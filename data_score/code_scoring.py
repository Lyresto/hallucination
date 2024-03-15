import json
import re
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import tiktoken
from matplotlib.patches import Patch
import matplotlib as mpl
import numpy as np
from fuzzywuzzy import fuzz
from tqdm import tqdm
from inject.hallucination_methods_logic import code_rmv_cmt
import tokenize
from io import BytesIO
from bytecode import Bytecode, Instr
import seaborn as sns


def tokenize_programming_language(code_):
    tokens = []
    for tok in tokenize.tokenize(BytesIO(code_.encode('utf-8')).readline):
        tokens.append(tok.string)
    return tokens


def get_prompt_length(**kwargs):
    prompt_ = kwargs.pop("prompt")
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(prompt_))
    # nlp = spacy.load("en_core_web_sm")
    # doc = nlp(prompt_)
    # tokens = [token.text for token in doc]
    # return len(tokens)
    # return prompt_length
    # return len(prompt_.strip().split(' '))


def get_code_length(**kwargs):
    code_ = kwargs.pop("code")
    code_lines = split_code_lines(code_)
    return len(tokenize_programming_language('\n'.join(code_lines))) - 1


def get_code_length_per_line(**kwargs):
    code_ = kwargs.pop("code")
    code_lines = split_code_lines(code_)
    return (len(tokenize_programming_language('\n'.join(code_lines))) - 1) \
        // len(code_lines)


def split_code_lines(code_: str):
    code_ = code_rmv_cmt(code_)
    code_lines = map(lambda s: s.strip(), code_.split('\n'))
    code_lines = list(filter(lambda line: len(line.strip()) > 0, code_lines))
    return code_lines


def get_similarity_between_prompt_and_code(**kwargs):
    code_ = kwargs.pop("code")
    prompt_ = kwargs.pop("prompt")
    return fuzz.ratio(prompt_.strip(), code_.strip())


def get_code_complexity(**kwargs):
    code_ = kwargs.pop("code")
    code_ = '\n' + code_rmv_cmt(code_)
    keywords = ["for ", "while ", "if ", "elif ", "else:", "import ", "and ", "or ", "in ", "not "]
    operators = ["+", "-", "*", "/", "%", "=", ".", "[", "]", "{", "}", "(", ")", ">", "<"]
    comp_ = 0
    for keyword in keywords:
        comp_ += len(re.findall(r'[ \t\n]' + keyword, code_))
    for operator in operators:
        operator = re.escape(operator)
        comp_ += len(re.findall(operator, code_))
    return comp_


def get_code_lines(**kwargs):
    code_ = kwargs.pop("code")
    return len(split_code_lines(code_))


def generate_byte_codes(code_):
    code_lines = list(filter(lambda line: len(line.strip()) > 0, code_.split('\n')))
    code_ = '\n'.join(code_lines)
    if code_.startswith('    ') or code_.startswith('\t'):
        code_ = 'def fun():\n' + code_
    compiled_code = compile(code_, '', 'exec')
    byte_codes = []
    for func_index in range(len(compiled_code.co_consts)):
        if isinstance(compiled_code.co_consts[func_index], type(compiled_code)):
            byte_codes.append(Bytecode.from_code(compiled_code.co_consts[func_index]))
    if 'def ' not in code_:
        byte_codes.append(Bytecode.from_code(compiled_code))
    return byte_codes


def get_basic_blocks_count(**kwargs):
    code_ = code_rmv_cmt(kwargs.pop("code"))
    byte_codes = generate_byte_codes(code_)
    block_count = 0
    for byte_code in byte_codes:
        for index, instr in enumerate(byte_code):
            if isinstance(instr, Instr):
                if 'JUMP' in instr.name or instr.name == 'FOR_ITER' or instr.name == 'CALL_FUNCTION':
                    block_count += 1
        block_count += 1
    return block_count


def get_method_call_count(**kwargs):
    code_ = code_rmv_cmt(kwargs.pop("code"))
    byte_codes = generate_byte_codes(code_)
    cnt = 0
    for byte_code in byte_codes:
        for index, instr in enumerate(byte_code):
            if isinstance(instr, Instr):
                if instr.name == 'CALL_METHOD':
                    cnt += 1
    return cnt


with open('../label_results/merged_data.json') as f:
    data = json.load(f)

with open('../label_results/merged_data_single.json') as f:
    ref_data = json.load(f)

models = ["codegen", "coderl", "gpt_0.0", "gpt_0.8"]
datasets = ["humaneval", "ds1000"]
metrics_handler = [get_prompt_length, get_code_length, get_code_length_per_line,
                   get_similarity_between_prompt_and_code, get_code_complexity,
                   get_code_lines, get_basic_blocks_count, get_method_call_count]

# with open('../code_alpaca_20k_filtered_6.json') as f:
#     data = json.load(f)
#
# abandon = 0
# for i, item in tqdm(enumerate(data)):
#     if "metrics" in item:
#         print(f'skip item{i}')
#         continue
#     prompt = item["instruction"] + "\n" + item["input"]
#     code = item["output"]
#     metrics = {}
#     try:
#         for handler in metrics_handler:
#             metric = handler(prompt=prompt, code=code)
#             name = ' '.join(handler.__name__.split('_')[1:])
#             metrics[name] = metric
#     except:
#         abandon += 1
#         continue
#     item["metrics"] = metrics
#     if (i + 1) % 100 == 0:
#         with open('../code_alpaca_20k_filtered_6.json', 'w+') as f:
#             f.write(json.dumps(data, indent=4))
#             print(f'successfully write json, cnt = {i + 1}, abandon = {abandon}')
#
# with open('../code_alpaca_20k_filtered_6.json', 'w+') as f:
#     f.write(json.dumps(data, indent=4))


results: list[list[int]]
results_2: list[list[int]]
results = [[] for _ in range(5)]
results_2 = [[] for _ in range(5)]
result_data = []
type_exist_cnt = []
for dataset in data:
    for problem in tqdm(data[dataset]):
        prompt = data[dataset][problem]["prompt"]
        code = data[dataset][problem]["reference"]
        prompt_length = ref_data[dataset][problem]["prompt_length"]
        # data[dataset][problem]["prompt_length"] = prompt_length
        labels = []
        for model in models:
            for idx, gen_code in enumerate(data[dataset][problem][model]):
                generate_code = gen_code["code"]
                # code_length = gen_code["code_length"]
                # gen_code["code_length"] = code_length
                labels_per_code = []
                for label in gen_code["labels"]:
                    if label["id"] == 5:
                        continue
                    labels.append(label["id"])
                    labels_per_code.append(label["id"])
                # for label in set(labels_per_code):
                #     results_2[label].append(code_length)
            # metric = models.index(model)
            # metric = datasets.index(dataset)
        for label in set(labels):
            results[label].append(prompt_length)

        label_cnt = [0] * 5
        for label in labels:
            label_cnt[label] += 1
        type_exist_cnt.append(list(map(lambda cnt: 0 if cnt == 0 else 1, label_cnt)))
        score = list(map(lambda cnt: 0.2 if cnt == 0 else 1 - 0.2 / cnt, label_cnt))
        metrics = {}
        for handler in metrics_handler:
            metric = handler(prompt=prompt, code=code)
            name = ' '.join(handler.__name__.split('_')[1:])
            metrics[name] = metric
        result_data.append({
            "metrics": metrics,
            "scores": score
        })


# with open('../label_results/merged_data_single.json', 'w+') as f:
#     f.write(json.dumps(data, indent=4))

with open('score_data_7.json', 'w+') as f:
    f.write(json.dumps(result_data, indent=4))
# type_exist_cnt = np.array(type_exist_cnt)
# print(np.mean(type_exist_cnt, axis=0))

# rg = (
#     min(min(result) for result in results),
#     max(max(result) for result in results)
# )
# bins = 2
# bar_width = (rg[0] + rg[1]) / bins
# hist_results = [np.histogram(d, bins=bins, range=rg)[0] for d in results]
# bin_edges = np.histogram([], bins=bins, range=rg)[1]
# bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
# total_results = np.sum(hist_results, axis=0)
# for i, it in enumerate(total_results):
#     if it == 0:
#         total_results[i] = 1
# fig, ax = plt.subplots(nrows=1, ncols=1)
# fig.set_size_inches(9, 6)
# # colors = ['#77bfa3', '#d8d890', '#a88fa4', '#c85d4b', '#6d92b6']
# colors = ["#a3caed", "#f9b48c"]
#
# types = ['Intent-conflicting', 'Inaccurate logic', 'Repetitive patterns',
#          'Incorrect API /\nvariable usage', 'Meaningless code']
# font = 'Times New Roman'
# mpl.rcParams['font.family'] = 'serif'
# mpl.rcParams['font.serif'] = font
#
# labels = []
# metrics = []
# for label, metric_arr in enumerate(results):
#     for metric in metric_arr:
#         labels.append(label)
#         metrics.append(metric)
# labels_2 = []
# metrics_2 = []
# for label, metric_arr in enumerate(results_2):
#     for metric in metric_arr:
#         labels_2.append(label)
#         metrics_2.append(metric)
# df = pd.DataFrame({'x': labels + labels_2, 'y': metrics + metrics_2,
#                    'hue': (["prompt"] * len(labels)) + (["code"] * len(labels_2))})
# print(len(labels), len(labels_2))
# sns.violinplot(x='x', y='y', ax=ax, hue='hue', data=df, palette=colors, linewidth=1.6)
# # for i, hall_type in enumerate(types):
# #     ax.bar(bin_centers * 7 + i * bar_width, hist_results[i] / total_results * 100,
# #            width=(bin_edges[1] - bin_edges[0]) * 0.9,
# #            alpha=1.0, color=colors[i])
# ax.set_ylabel("Length (#Tokens)", rotation=90, fontfamily=font, fontsize=16, labelpad=14)
# ax.set_xlabel("", fontfamily=font, fontsize=16, labelpad=14)
# new_xticks = ax.get_xticks()  # bin_centers * 7 + 2 * bar_width
# ax.set_xticks(new_xticks)
# ax.set_xticklabels(types,  # ["CodeGen", "CodeRL", "ChatGPT-temp-0.8", "ChatGPT-greedy"],
#                    fontfamily=font, fontsize=14.5)
# ax.tick_params(axis='x', pad=6, length=6)
# ax.set_yticks(ax.get_yticks())
# ax.set_yticklabels(ax.get_yticklabels(), fontfamily=font, fontsize=14)
# # ax.tick_params(axis='x', which='both', bottom=False, top=False)
# ax.grid(True, axis='y')
# ax.set_axisbelow(True)
# plt.ylim(-180, 1400)
# legend_patches = [Patch(color=color, label=["Prompt", "Code"][i]) for i, color in enumerate(colors)]
# legend = ax.legend(handles=legend_patches, fontsize=16)
# plt.tight_layout()
# plt.show()
# fig.savefig('C:/Users/Dell/Desktop/代码分析/figures/hall_type_by_length.pdf', format='pdf')
