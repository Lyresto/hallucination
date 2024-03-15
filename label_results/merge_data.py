import json
import os
from math import sqrt

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Patch

datasets = ["humaneval", "ds1000"]
models = ["codegen", "coderl", "gpt_0.0", "gpt_0.8"]


def cut_code(code_: str, start_, end_):
    code_lines = code_.split('\n')
    return '\n'.join(code_lines[start_ - 1: end_])


"""
{
    "humaneval": {
        "humaneval/0": {
            "prompt": "...",
            "reference": "...",
            "codegen": [
                {
                    "code": "...",
                    "labels": [
                        {
                            "id": 0,
                            "start": 1,
                            "end": 5
                        },
                        ...
                    ]
                },
                ...
            ]
            "coderl": ...
        }
        "humaneval/1": ...
    }
    "ds1000": ...
}
"""

old_id2new_id = {
    "1": 1, "2": 0, "3": 0, "4": 2, "5": 4, "6": 0, "7": 4, "8": 3,
    "9": 2, "10": 3, "11": 3, "12": 3, "13": 3, "14": 2, "15": 5
}
types = ['Intent-conflicting', 'Inaccurate logic', 'Repetitive patterns',
         'Incorrect API /\nvariable usage', 'Meaningless code']

results = {}
id_cnt = [0] * 6
model_cnt = {model: 0 for model in models}
fail_codes = []
fig_results: list[list[int]]
fig_results = [[0, 0, 0] for _ in range(5)]
for dataset in datasets:
    results[dataset] = {}
    results_dataset = results[dataset]
    if dataset == 'humaneval':
        with open('problem/humaneval.jsonl') as f:
            for line in f:
                parsed_line = json.loads(line)
                problem_id = parsed_line["task_id"]
                results_dataset[problem_id] = {
                    "prompt": parsed_line["prompt"],
                    "reference": parsed_line["canonical_solution"]
                }
    else:
        for lib in os.listdir('problem/ds1000'):
            for problem in os.listdir('problem/ds1000/' + lib):
                problem_dir = 'problem/ds1000/' + lib + '/' + problem
                problem_id = lib + '.' + problem
                results_dataset[problem_id] = {}
                try:
                    with open(problem_dir + '/prompt.txt') as f:
                        results_dataset[problem_id]["prompt"] = f.read()
                except UnicodeDecodeError:
                    with open(problem_dir + '/prompt.txt', encoding='utf8') as f:
                        results_dataset[problem_id]["prompt"] = f.read()
                with open(problem_dir + '/reference_code.txt') as f:
                    results_dataset[problem_id]["reference"] = f.read()
    for model in models:
        with open('result/' + dataset + '/' + model + '_result.json') as f:
            label_result = json.load(f)
        with open('judge/' + dataset + '/' + model + '.json') as f:
            judge_result = json.load(f)
        id_code_tuple = []
        if dataset == 'humaneval':
            with open('code/humaneval/' + model + '.jsonl') as f:
                for line in f:
                    parsed_line = json.loads(line)
                    id_code_tuple.append((parsed_line["task_id"], parsed_line["completion"]))
        else:
            for lib in os.listdir('code/ds1000/' + model):
                for problem in os.listdir('code/ds1000/' + model + '/' + lib):
                    problem_dir = 'code/ds1000/' + model + '/' + lib + '/' + problem
                    problem_id = lib + '.' + problem
                    with open(problem_dir + '/0.py') as f:
                        code = f.read()
                    id_code_tuple.append((problem_id, code))
        for idx, label_result_item in enumerate(label_result):
            problem_id, code = id_code_tuple[idx]
            judge_result_item = judge_result[idx]
            pass_all = judge_result_item["pass"] == judge_result_item["all"]
            results_dataset_problem = results_dataset[problem_id]
            if model not in results_dataset_problem:
                results_dataset_problem[model] = []
            # # fixme:
            else:
                continue
            model_cnt[model] += 1
            labels = []
            for label_result_item_item in label_result_item:
                message = label_result_item_item["line"].split("=")
                if "-" in message[0]:
                    start_end = message[0].split("-")
                    start = int(start_end[0])
                    end = int(start_end[1])
                else:
                    start = end = int(message[0])
                old_hall_id = int(message[1])
                if old_hall_id == 5 and ('print(' in cut_code(code, start, end) or
                                         'assert' in cut_code(code, start, end)):
                    continue
                if "version" in label_result_item_item and label_result_item_item["version"] == "2.0":
                    hall_id = int(message[1])
                else:
                    hall_id = old_id2new_id[message[1]]
                labels.append({
                    "id": hall_id,
                    "start": start,
                    "end": end
                })
                id_cnt[labels[-1]["id"]] += 1
            results_dataset_problem[model].append({
                "code": code,
                "pass all": pass_all,
                "labels": labels
            })
            for label in set([label["id"] for label in labels]):
                if label >= 5:
                    continue
                if judge_result_item["pass"] == judge_result_item["all"]:
                    pass_type = 2

                elif 0 < judge_result_item["pass"] < judge_result_item["all"]:
                    pass_type = 1
                else:
                    pass_type = 0
                fig_results[label][pass_type] += 1
            if not pass_all:
                fail_codes.append(int(len(labels) > 0))

print(id_cnt)
print(model_cnt)
print(sum(model_cnt.values()))
print(sum(id_cnt))
print(fig_results)
print(100 - sum(fail_codes) / len(fail_codes) * 100)
print(len(fail_codes))
# with open('merged_data_single.json', 'w+') as f:
#     f.write(json.dumps(results, indent=4))

font = 'Times New Roman'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = font
colors = ["#339966", "#9a9a9a", '#696969']

pass_rate = [it[2] / sum(it) * 100 for it in fig_results]
partial_pass_rate = [it[1] / sum(it) * 100 for it in fig_results]
all_fail_rate = [100 - sum(it[1:]) / sum(it) * 100 for it in fig_results]
print(pass_rate, partial_pass_rate, all_fail_rate)
pass_rate.reverse()
partial_pass_rate.reverse()
all_fail_rate.reverse()
types.reverse()
not_all_fail_rate = [pass_rate[i] + partial_pass_rate[i] for i in range(5)]

fig, ax = plt.subplots()
fig.set_size_inches(9, 4.5)
alpha = 1.0
height = 0.7
bar1 = ax.barh(types, pass_rate, color=colors[0], height=height, alpha=alpha)
bar2 = ax.barh(types, partial_pass_rate, color=colors[1], left=pass_rate, height=height, alpha=alpha)
bar3 = ax.barh(types, all_fail_rate, color=colors[2], left=not_all_fail_rate, height=height, alpha=alpha)


text_color = '#FFFFFF'
for bar, rate in zip(bar1, pass_rate):
    text_x = sqrt(bar.get_width())
    text_y = bar.get_y() + bar.get_height() / 2
    ax.text(text_x, text_y, f'{round(rate, 2)}%', ha='center', va='center',
            color=text_color, fontsize=14, fontfamily=font)

for bar, rate in zip(bar2, partial_pass_rate):
    text_x = sqrt((bar.get_width() + bar.get_x()) * bar.get_x())
    text_y = bar.get_y() + bar.get_height() / 2
    ax.text(text_x, text_y, f'{round(rate, 2)}%', ha='center', va='center',
            color=text_color, fontsize=14, fontfamily=font)

for bar, rate in zip(bar3, all_fail_rate):
    text_x = sqrt((bar.get_width() + bar.get_x()) * bar.get_x())
    if rate == all_fail_rate[-1]:
        text_x = bar.get_x() + 10
    text_y = bar.get_y() + bar.get_height() / 2
    ax.text(text_x, text_y, f'{round(rate, 2)}%', ha='center', va='center',
            color=text_color, fontsize=14, fontfamily=font)


ax.set_ylabel("", rotation=90, fontfamily=font, fontsize=16, labelpad=14)
ax.set_xlabel("Proportion (%)", fontfamily=font, fontsize=16, labelpad=14)
new_xticks = ax.get_xticks()
ax.set_xticks(new_xticks)
ax.set_xticklabels(ax.get_xticklabels(), fontfamily=font, fontsize=14.5)
ax.tick_params(axis='x', pad=6)
plt.xscale('log')
ax.set_yticks(ax.get_yticks())
ax.set_yticklabels(ax.get_yticklabels(), fontfamily=font, fontsize=15)
legend_patches = [Patch(color=color, label=["All Passed", "Partially Passed", "All Failed"][i]) for i, color in enumerate(colors)]
ax.legend(handles=legend_patches, fontsize=12, loc='upper right')
plt.xlim(1, 100)
ax.grid(True, axis='x')
ax.set_axisbelow(True)
plt.tight_layout()
plt.show()
# fig.savefig('C:/Users/Dell/Desktop/代码分析/figures/pass_rate_by_hall_type.pdf', format='pdf')
