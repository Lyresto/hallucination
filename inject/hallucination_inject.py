import json
import os.path
import time

from code_obtain import call_gpt
from hallucination_methods_logic import gen_prompt, extract_code, debug, \
    generate_copy_of_input, generate_function_duplication, generate_unlimited_code, \
    generate_code_with_invalid_identifier, generate_invalid_code

funcs = [generate_copy_of_input, generate_function_duplication, generate_unlimited_code,
         generate_code_with_invalid_identifier, generate_invalid_code]
with open("code_alpaca_20k_filtered_7.json") as f:
    data = json.load(f)
with open("methods.json", encoding='utf8') as f:
    methods = json.load(f)

result_path = '../generate_results/generate1.json'
if os.path.exists(result_path):
    with open(result_path) as f:
        results = json.load(f)
else:
    results = {}


for index in range(0, len(data)):
    item = data[index]
    hall_id = item["distributed type"]
    hall_sub_id = item["distributed subtype"]
    if debug:
        if hall_id != 0 or hall_sub_id != 0:
            continue
        print(hall_id, hall_sub_id)
    method = methods[hall_id][hall_sub_id]
    if not method["use model"]:
        if str(index) in results:
            print(f'[data{index + 1}/{len(data)}] exists, skip')
            continue
            # print(f'[data{index + 1}/{len(data)}] re-generate')
        if debug:
            print(item["instruction"], '\n')
            print(item["input"])
        method_name = method["method"].split('|')[0]
        param = method["method"].split('|')[1]
        func = None
        for f in funcs:
            if f.__name__ == method_name:
                func = f
                break
        if func is None:
            exit(-111)
        print(f'[data{index + 1}/{len(data)}]')
        if param == "code":
            hall_code = f(item["output"])
        elif param == "input":
            hall_code = f(item["input"])
        else:
            exit(-222)
        hall_code = hall_code.strip()
        results[str(index)] = {
            "index": index,
            "use model": False,
            "hall code": hall_code
        }
    else:
        # if str(index) in results and results[str(index)]["succeed"]:
        #     print(f'[data{index + 1}/{len(data)}] exists, skip')
        #     continue
        # # fixme:
        # if hall_id == 0 and hall_sub_id == 1:
        #     method = methods[0][0]
        #     hall_id = 0
        #     hall_sub_id = 0
        prompt, example_index = gen_prompt(method, item)
        if debug:
            print(prompt, "\n\n\n")
            s = input()
            if s == '-1':
                break
            continue

        if f'{hall_id}{hall_sub_id}{example_index}' in ['400', '401', '402', '312']:
            model_version = 4
            generate_codes_num = 2
        else:
            model_version = 3.5
            generate_codes_num = 5
        hall_codes = []
        ret_contents = []
        # if str(index) in results:
        #     hall_codes = results[str(index)]["hall codes"]
        #     ret_contents = results[str(index)]["outputs"]
        retry = 0
        succeed = True
        while True:
            print(f'[data{index + 1}/{len(data)}::'
                  f'code{len(hall_codes) + 1}/{generate_codes_num}::try{retry + 1}]', end=' ')
            if model_version == 4:
                ret_content = call_gpt(prompt, temp=1.0, model='gpt-4')
            else:
                ret_content = call_gpt(prompt, temp=1.0)
            if debug:
                print(ret_content)
            try:
                hall_code = extract_code(ret_content, hall_id, hall_sub_id)
            except Exception as e:
                hall_code = None
            if hall_code is not None:
                hall_codes.append(hall_code)
                ret_contents.append(ret_content)
                retry = 0
            else:
                retry += 1
                if retry == generate_codes_num * 2:
                    print("reached maximum retry!")
                    succeed = False
                    break
            if len(hall_codes) == generate_codes_num:
                break
        results[str(index)] = {
            "index": index,
            "use model": True,
            "model": model_version,
            "outputs": ret_contents,
            "succeed": succeed,
            "hall codes": hall_codes
        }
        with open(result_path, 'w+') as f:
            f.write(json.dumps(results, indent=4))
    # if debug:
    #     print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hall code>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n" + str(hall_code))
    #     print("\n====================================================================")
    #     s = input()
    #     if s == '-1':
    #         break

# with open(result_path, 'w+') as f:
#     f.write(json.dumps(results, indent=4))
