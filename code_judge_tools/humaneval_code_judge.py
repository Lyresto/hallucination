import json
import subprocess
import threading
import re
import os
import time

import xlrd


def execute_code():
    threshold = 1000
    character_count = 0

    process = subprocess.Popen(["py", "-3.8-64", "../testFolder/tmp2.py"],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def terminate(process_):
        print("timeout.")
        process_.terminate()

    timer = threading.Timer(5, terminate, args=[process])
    timer.start()
    cnt = 0
    while True:
        out = process.stdout.readline()
        err = process.stderr.readline()
        if err:
            cnt = 0
            break
        if not out:
            break
        try:
            out = out.decode(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        character_count += len(out)
        if out.strip() == "pass":
            cnt += 1
        if character_count > threshold:
            process.kill()
            break
    timer.cancel()
    return cnt


def fix_code_v2(code_: str, prompt_: str = None):
    funcs = []
    start = 0
    if prompt_ is not None:
        prompts = prompt_.split("\n")
        func_def = ""
        for p in prompts:
            if p.strip().startswith("def "):
                func_def = p.strip()
                func_def = func_def[0: func_def.index("(")]
        insert = func_def not in code_
    else:
        insert = False
    while True:
        end = code_.find("def ", start + 1)
        if end == -1:
            funcs.append(fix_code(code_[start: len(code_)], prompt_, insert))
            break
        funcs.append(fix_code(code_[start: end], prompt_, insert))
        start = end
    return '\n'.join(funcs)


def fix_code(code_: str, prompt_: str = None, insert_func_name: bool = False):
    indent = ["if", "elif", "else", "for", "while", "def", "try", "except"]
    coll = [",", "(", "[", "{", "\\", ":"]
    codes = code_.split("\n")
    up_space = 0
    up_ident = False
    up_collection = False
    in_note = False
    for i in range(len(codes)):
        c = codes[i]
        if c.strip() == 'if __name__ == "__main__":':
            codes = codes[: i]
            break
        cur_space = len(c) - len(c.lstrip())
        if (c.strip().startswith("'''") or c.strip().startswith("\"\"\"")) and not in_note:
            in_note = True
            continue
        elif (c.strip().endswith("'''") or c.strip().endswith("\"\"\"")) and in_note:
            in_note = False
            continue
        if len(c.strip()) == 0 or c.strip().startswith('#') or in_note:
            continue
        if (up_ident and cur_space - up_space != 4) or \
                (not up_ident and cur_space > up_space and not up_collection):
            if up_ident:
                dist = up_space + 4 - cur_space
            else:
                dist = up_space - cur_space
            for j in range(i, len(codes)):
                if dist > 0:
                    codes[j] = ''.join([' '] * dist) + codes[j]
                else:
                    space = len(codes[j]) - len(codes[j].lstrip())
                    codes[j] = codes[j][min(abs(dist), space):]
        c = codes[i]
        up_space = len(c) - len(c.lstrip())
        up_ident = any(c.strip().startswith(ide) for ide in indent)
        up_collection = any(c.strip().endswith(col_) for col_ in coll)
    if prompt_ is not None and "import" not in code_ and insert_func_name:
        prompts = prompt_.split("\n")
        func_def = ""
        for p in prompts:
            if p.strip().startswith("def "):
                func_def = p.strip()
        if code_.find("def ") < 0 and code_.find("print(") < 0:
            for i in range(len(codes)):
                codes[i] = "    " + codes[i]
            codes = [func_def] + codes
    return '\n'.join(codes) + "\n\n"


def fix_check_func(func: str):
    start = func.find("def check")
    head = func[: start]
    func = func[start:]
    func_lines = func.strip().split("\n")
    new_func_lines = [func_lines[0], "    try:"]
    up_assert = False
    up_space = 0
    up_candidate = False
    for line_ in func_lines[1: len(func_lines)]:
        cur_space = len(line_) - len(line_.lstrip())
        if line_.lstrip().startswith("assert"):
            cur_assert = True
        else:
            cur_assert = False
        if up_assert and (cur_space < up_space or cur_assert or cur_space == 4):
            if up_candidate:
                new_func_lines.append("        print(\"pass\")\n    except:\n        print(\"not pass\")\n    try:")
            else:
                new_func_lines.append("        pass\n    except:\n        pass\n    try:")
            up_candidate = False
            up_assert = False
        if 'candidate(' in line_:
            up_candidate = True
        new_func_lines.append("    " + line_)
        up_assert = cur_assert or up_assert
        up_space = cur_space
    if up_assert and up_candidate:
        new_func_lines.append("        print(\"pass\")\n    except:\n        print(\"not pass\")")
    else:
        new_func_lines.append("        pass\n    except:\n        pass")
    new_func = '\n'.join(new_func_lines)
    return head + "\n" + new_func


if __name__ == '__main__':
    base_project_dir = "D:\\代码分析\\数据\\CodeGen_Results\\Human-eval"
    configs = {}
    result = []
    # model = ["chatgpt", "codegeex2", "codegen25"]

    with open(base_project_dir + "\\data\\human-eval-v2-20210705.jsonl") as config_file:
        for line in config_file:
            config_line = json.loads(line)
            configs[config_line["task_id"]] = config_line
    codes_result = []
    model = "coderl"
    with open(
            "modified.jsonl",
            encoding='utf8') as f:
        for line in f:
            codes_result.append(json.loads(line))
    # with xlrd.open_workbook("C:\\Users\\Dell\\Desktop\\代码分析\\数据\\weakness\\humaneval_new.xlsx") as code_file:
    cnt_all = []
    # index = 687
    for line in codes_result:
        # if index > 0:
        #     index -= 1
        #     continue
        taskId = line["task_id"]
        config = configs[taskId]
        code = line["completion"]
        judge_code = "from typing import List, Tuple, Optional, Any\n\n\n" + \
                     fix_code_v2(code, config["prompt"]) \
                     + "\n" + fix_check_func(config["test"]) + "\n" \
                     + "check(" + config["entry_point"] + ")\n"
        try:
            with open("../testFolder/tmp2.py", 'w+') as temp_file:
                temp_file.write(judge_code)
        except UnicodeEncodeError:
            with open("../testFolder/tmp2.py", 'w+', encoding='utf-8') as temp_file:
                temp_file.write(judge_code)
        pss_cnt = execute_code()
        cnt_all.append(pss_cnt)
        all_case = len(re.findall(r'candidate\(', config["test"]))
        print(f'{taskId}: {pss_cnt} / {all_case}')
        if all_case < pss_cnt:
            print("error pass cnt")
            exit(-1)
        result.append({
            "pass": pss_cnt,
            "all": all_case
        })

    with open(f'modified_result.json', 'w+') as f:
        f.write(json.dumps(result))
