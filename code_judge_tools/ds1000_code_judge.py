import json
import os
import pickle
import re
import shutil
import subprocess
import threading
from humaneval_code_judge import fix_code_v2
import xlwt
from colorama import Fore


def insert_code_2_context(context_: str, code_: str):
    context_lines = context_.split('\n')
    insert_line = 0
    if "plt.show()" in code_:
        code_ = code_.replace("plt.show()", "")
    if "\nEND SOLUTION" in code_:
        code_ = code_.replace("\nEND SOLUTION", "")
    for i_, line_ in enumerate(context_lines):
        if line_ == "[insert]":
            insert_line = i_
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


def main():
    sample_dir = base_dir + "\\" + model + "-sample"
    judge_results = []
    for lib in os.listdir(sample_dir):
        if lib == ".idea":
            continue
        for pid in os.listdir(sample_dir + "\\" + lib):

            problem_dir = sample_dir + "\\" + lib + "\\" + pid

            print(lib + "_" + pid + " start.")
            with open(problem_dir + "\\5.py") as f:
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
                    test_code = "import pickle\n\n" + test_code
                    result_path_enc = re.sub('\\\\', '\\\\\\\\', result_path)
                    answer_path_enc = re.sub('\\\\', '\\\\\\\\', answer_path)
                    test_code += f"\n\nwith open('{result_path_enc}', 'rb+') as f:\n" + \
                                 "    result = pickle.load(f)\n" + \
                                 f"\nwith open('{answer_path_enc}', 'rb+') as f:\n" + \
                                 "    answer = pickle.load(f)\n" + \
                                 "\nprint(test(result, answer))\n"
                    with open("../testFolder/tmp.py", 'w', encoding='utf8') as f:
                        f.write(test_code)
                    process = subprocess.Popen(["D:\\python\\pythonProject\\venv\\Scripts\\python.exe",
                                                "../testFolder/tmp.py"], cwd=problem_dir,
                                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    def terminate(process_):
                        print("extra test timeout.")
                        process_.terminate()

                    timer = threading.Timer(5, terminate, args=[process])
                    timer.start()
                    while True:
                        err = process.stderr.readline().decode('utf8')
                        out = process.stdout.readline().decode('utf8')
                        if not out:
                            break
                        if len(out.strip()) > 0:
                            if out.strip() == '1':
                                print('extra test pass!')
                                pass_cnt += 1
                            else:
                                print(f'extra test: {out}')
                            break
                        elif len(err.strip()) > 0:
                            if "Error" in err:
                                print(f'extra test: {err}')
                                break
                    timer.cancel()

            with open(problem_dir + "\\passed_testcases.txt", 'w+') as f:
                f.write(str(pass_cnt) + "/" + str(test_case_num))
            print(lib + "_" + pid + ": " + str(pass_cnt) + "/" + str(test_case_num))
            judge_results.append({
                "pass": pass_cnt,
                "all": test_case_num
            })

    with open(f'result.json', 'w+') as f:
        f.write(json.dumps(judge_results))


if __name__ == '__main__':
    base_dir = "path/to/DS-1000"
    model = "your_model"
    main()
