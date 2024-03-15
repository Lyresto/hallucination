import json
import os
import pickle
import shutil
import subprocess
import threading
from humaneval_code_judge import fix_code_v2
import xlwt
from colorama import Fore

base_dir = "C:\\Users\\Dell\\Desktop\\代码分析\\数据\\CodeGen_Results\\DS-1000"
model = "coderl_temp0.8_outputs"
sample_dir = base_dir + "\\" + model + "-sample"

# label_result_path = "D:\\Java\\Idea_project\\code\\src\\main\\java\\com\\code\\code\\ds1000_codegen_result.json"
#
# with open(label_result_path) as f:
#     label_result = json.load(f)
excel = xlwt.Workbook('utf-8')
sheet = excel.add_sheet('result')
id2des = {"1": "相关逻辑错误", "2": "主题无关", "3": "局部无关", "4": "重复生成", "5": "无意义代码",
          "6": "多余输入语句", "7": "无效生成", "8": "使用错误标识符", "9": "无限生成", "10": "库函数选取错误",
          "11": "库函数多余调用", "12": "库函数传参错误", "13": "库函数多余传参", "14": "复制题目代码",
          "15": "特例下生成"}
id_cnt = {hall_id: 0 for hall_id in id2des}


def insert_code_2_context(context_: str, code_: str):
    context_lines = context_.split('\n')
    insert_line = 0
    # code_ = fix_code_v2(code_)
    if "plt.show()" in code_:
        code_ = code_.replace("plt.show()", "")
    if "\nEND SOLUTION" in code_:
        code_ = code_.replace("\nEND SOLUTION", "")
    for i_, line_ in enumerate(context_lines):
        if line_ == "[insert]":
            insert_line = i_
    # search_line = insert_line - 1
    # while search_line >= 0:
    #     if context_lines[search_line].strip().startswith('#') or len(context_lines[search_line].strip()) == 0:
    #         search_line -= 1
    #     else:
    #         break
    # if insert_line > 0 and (context_lines[search_line].startswith("def ")
    #                         or context_lines[search_line][0] == ' ' or context_lines[search_line][0] == '\t') \
    #         and code_[0] != ' ' and code_[0] != '\t':
    #     code_lines = code_.split('\n')
    #     code_ = '    ' + '\n    '.join(code_lines)
    context_lines[insert_line] = code_
    return fix_code_v2('\n'.join(context_lines[0: insert_line + 1])) \
        + '\n' + '\n'.join(context_lines[insert_line + 1:])


def extract_code(txt: str):
    txt = txt.replace('\t', '    ')
    if '```' not in txt:
        return txt
    else:
        start = -1
        end = -1
        in_code = False
        for i_, c in enumerate(list(txt)):
            if txt[i_: i_ + 3] == '```':
                in_code = True
            if in_code and start < 0 and c == '\n':
                start = i_ + 1
            if start > 0 and txt[i_: i_ + 3] == '```':
                end = i_
                break
        return txt[start: end]


sum_all = 0
sum_pass = 0
problem_index = 0
line = 0
judge_results = []
for lib in os.listdir(sample_dir):
    if lib == ".idea":
        continue
    if lib != "Scipy":
        continue
    for pid in os.listdir(sample_dir + "\\" + lib):
        if pid != "q30":
            continue

        problem_dir = sample_dir + "\\" + lib + "\\" + pid

        # for hall in label_result[problem_index]:
        #     info = hall["line"].split("=")
        #     sheet.write(line, 0, lib)
        #     sheet.write(line, 1, pid)
        #     try:
        #         with open(problem_dir + "\\prompt.txt") as f:
        #             sheet.write(line, 2, f.read())
        #     except UnicodeError:
        #         with open(problem_dir + "\\prompt.txt", encoding='utf8') as f:
        #             sheet.write(line, 2, f.read())
        #     with open(problem_dir + "\\0.py") as f:
        #         sheet.write(line, 3, f.read())
        #     sheet.write(line, 4, id2des[info[1]])
        #     id_cnt[info[1]] += 1
        #     sheet.write(line, 6, info[0].replace("-", "~"))
        #     line += 1
        # problem_index += 1

        # if os.path.exists(problem_dir + "\\passed_testcases.txt"):
        #     print(lib + "_" + pid + " skip.")
        #     continue

        #     with open(problem_dir + "\\passed_testcases.txt") as f:
        #         data = f.read().split("/")
        #         sum_pass += int(data[0])
        #         sum_all += int(data[1])
        #     continue
        print(lib + "_" + pid + " start.")
        with open(problem_dir + "\\0.py") as f:
            insert_code = extract_code(f.read())
        with open(problem_dir + "\\code_context.txt") as f:
            raw_context = f.read()
            context = insert_code_2_context(raw_context, insert_code)
        with open(problem_dir + "\\tmp.py", 'w+') as f:
            f.write(context)
        if os.path.exists(problem_dir + "\\result"):
            shutil.rmtree(problem_dir + "\\result")
        os.mkdir(problem_dir + "\\result")
        for i in range(len(os.listdir(problem_dir + "\\ans"))):
            # progress = subprocess.Popen(["D:\\python\\pythonProject\\venv\\Scripts\\python.exe",
            #                              problem_dir + "\\test_generate_pickle.py", "--test_case",
            #                              str(i + 1)], cwd=problem_dir)
            # progress.wait()
            process = subprocess.Popen(["D:\\python\\pythonProject\\venv\\Scripts\\python.exe",
                                        problem_dir + "\\tmp.py", "--test_case", str(i + 1)],
                                       cwd=problem_dir, stderr=subprocess.PIPE)
            trace = ""

            def terminate(process_):
                print("timeout.")
                process_.terminate()
            timer = threading.Timer(5, terminate, args=[process])
            timer.start()
            while process.poll() is None:
                err = process.stderr.readline().decode('utf8')
                if "line" in err:
                    trace = err
                if "Error" in err:
                    if "NameError" in err or "AssertionError" in err \
                            or "AttributeError" in err or "KeyError" in err \
                            or "ValueError" in err or "TypeError" in err:
                        print(err)
                    else:
                        print(Fore.RED + trace + err, end='')
                        print(Fore.RESET)
            timer.cancel()

        test_case_num = len(os.listdir(problem_dir + "\\input"))
        pass_cnt = 0
        for i in range(1, test_case_num + 1):
            answer_path = problem_dir + "\\ans\\ans" + str(i) + ".pkl"
            result_path = problem_dir + "\\result\\result_" + str(i) + ".pkl"
            input_path = problem_dir + "\\input\\input" + str(i) + ".pkl"
            if not os.path.exists(result_path):
                continue
            with open(input_path, 'rb+') as f:
                ipt = pickle.load(f)
                print(ipt)
            with open(answer_path, 'rb+') as f:
                answer = pickle.load(f)
                print("answer(line1): ", end='')
                print(answer)
            with open(result_path, 'rb+') as f:
                if len(f.read()) == 0:
                    continue
                f.seek(0)
                try:
                    result = pickle.load(f)
                except:
                    continue
                print("result(line1): ", end='')
                print(result)
            if str(answer) == str(result) or (answer is None and result is True):
                pass_cnt += 1
            else:
                with open(problem_dir + "\\test_code.py") as f:
                    test_code = f.read()
                with open("../testFolder/tmp.py", 'w') as f:
                    f.write(test_code)
                try:
                    from testFolder.tmp import test
                    test_res = test(result, answer)
                    pass_cnt += test_res
                except:
                    pass
        with open(problem_dir + "\\passed_testcases.txt", 'w+') as f:
            f.write(str(pass_cnt) + "/" + str(test_case_num))
        print(lib + "_" + pid + ": " + str(pass_cnt) + "/" + str(test_case_num))
        judge_results.append({
            "pass": pass_cnt,
            "all": test_case_num
        })

with open(f'result.json', 'w+') as f:
    f.write(json.dumps(judge_results))

