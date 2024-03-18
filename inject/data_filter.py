import json
import re
import os
import subprocess
import threading

from tqdm import tqdm

run_well = True


def is_python_file(_problem):
    try:
        with open('../testFolder/tmp.py', 'w+') as _f:
            _f.write(_problem["output"])
    except UnicodeEncodeError:
        with open('../testFolder/tmp.py', 'w+', encoding='utf8') as _f:
            _f.write(_problem["output"])
    process = subprocess.Popen(["D:\\python\\pythonProject\\venv\\Scripts\\python.exe",
                                ".\\tmp.py"], cwd=".\\testFolder",
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    global run_well
    run_well = True

    def terminate(process_):
        print("timeout.")
        global run_well
        run_well = False
        process_.terminate()

    timer = threading.Timer(5, terminate, args=[process])
    timer.start()
    while process.poll() is None:
        err = process.stderr.readline().decode('utf8')
        if "Error" in err:
            if "ImportError" in err or "NameError" in err:
                continue
            else:
                timer.cancel()
                return False
    timer.cancel()
    return run_well


def has_excluded_languages(_problem):
    excluded_languages = ["C", "C++", "C#", "JAVA", "JS", "JAVASCRIPT",
                          "SQL", "MATLAB", "R", "XML", "HTML", "CSS", "MYSQL",
                          "RUBY", "PASCAL", "PHP", "VERILOG", "VHDL", "MIPS",
                          "VISUAL BASIC", "PERL", "GO", "SWIFT", "JSP", "LINQ",
                          "JULIA", "TYPESCRIPT", "KOTLIN", "MONGODB", "MONGOOSE"]
    for lang in excluded_languages:
        if (' ' + lang + ' ') in _problem["instruction"].upper() or \
                (' ' + lang + '.') in _problem["instruction"].upper():
            return True
    return False


def has_python_reversed_words(_problem):
    typical_reversed_words = ["import", "if", "elif", "else", "for", "while",
                              "def", "try", "except", "return"]
    if "=" in _problem["output"]:
        return True
    for w in typical_reversed_words:
        if (w + ' ') in _problem["output"]:
            return True
    return False


def main():
    with open("code_alpaca_20k.json") as f:
        problems = json.load(f)

    filtered_problems = []
    cnt = 0
    for problem in tqdm(problems):
        key_words = ["following code", "rewrite", "modify", "edit", "update",
                     "given code", "refactor", "complete"]
        if any(key_word in problem["instruction"].lower() for key_word in key_words) and len(problem["input"]) == 0:
            continue
        filtered_problems.append(problem)

        python = False
        if 10 <= len(list(problem["output"])) <= 2500:
            if not has_excluded_languages(problem) and has_python_reversed_words(problem) and is_python_file(problem):
                python = True
            else:
                python = False
            if python:
                filtered_problems.append(problem)
                if len(filtered_problems) % 200 == 0:
                    print("get " + str(len(filtered_problems)) + " in " + str(cnt) + " cases")
                    with open(output_file, 'w+') as f:
                        f.write(json.dumps(filtered_problems, indent=4))

    with open(output_file, 'w+') as f:
        f.write(json.dumps(filtered_problems, indent=4))


if __name__ == '__main__':
    output_file = 'code_alpaca_20k_filtered_7.json'
    main()
