import json
import random
import re

import pulp


def maximize_total_score(data_, groups_, scores_, capacities_, exclusions_):
    # 创建一个线性规划问题
    prob = pulp.LpProblem("Maximize_Total_Score", pulp.LpMaximize)

    # 创建数据分配变量
    x = pulp.LpVariable.dicts("x", ((i, j) for i in data_ for j in groups_), 0, 1, pulp.LpBinary)

    # 添加目标函数
    prob += pulp.lpSum(scores_[i][j] * x[i, j] for i in data_ for j in groups_)

    # 添加约束条件
    for i in data_:
        prob += pulp.lpSum(x[i, j] for j in groups_) == 1  # 每个数据项只能分配到一个组

    for j in groups_:
        prob += pulp.lpSum(x[i, j] for i in data_) == capacities_[j]  # 每个组的容量约束

    for i in data_:
        prob += pulp.lpSum(x[i, j] * exclusions_[i][j] for j in groups_) == 0

    # 求解线性规划问题
    print("start solving...")
    prob.solve()

    # 输出结果
    result_ = {}
    for i in data_:
        for j in groups_:
            if pulp.value(x[i, j]) == 1:
                result_[i] = j

    return result_


with open('code_alpaca_20k_filtered_7.json') as f:
    dataset = json.load(f)
source_capa = [681, 674, 366, 320, 68]

data = [i for i in range(len(dataset))]
groups = [0, 1, 2, 3, 4]
scores = []
exclusions = []
capacities = [len(dataset) * it // sum(source_capa) for it in source_capa]
capacities[-1] = len(dataset) - sum(capacities[:-1])

for item in dataset:
    score = item["scores"]
    recommend = item["recommend"]
    scores.append([score[i] + recommend[i] for i in range(len(score))])
    exclusions.append(item["exclusion"])


result = maximize_total_score(data, groups, scores, capacities, exclusions)
print(result)

for i, item in enumerate(dataset):
    item["distributed type"] = result[i]


# counter = []
# new_res = []
# for i, item in enumerate(dataset):
#     output = item["output"]
#     if item["distributed type"] == 0:
#         if len(item["input"]) <= 27:
#             counter.append(1)
#             subtype = 0
#         else:
#             counter.append(0)
#             subtype = 1
#         item["distributed subtype"] = subtype
#
#     if item["distributed type"] == 4:
#         if item["metrics"]["code lines"] >= 4 and i % 13 >= 5:
#             counter.append(1)
#             subtype = 1
#         else:
#             counter.append(0)
#             subtype = 0
#         item["distributed subtype"] = subtype
#
#     if item["distributed type"] == 3:
#         exclude_libs = ['string', 'os', 'math', 'sqrt', 'sys', 'e']
#         if "import " in output and all([('import ' + lib) not in output for lib in exclude_libs]):
#             counter.append(0)
#             subtype = 1
#         else:
#             counter.append(1)
#             subtype = 0
#         item["distributed subtype"] = subtype
#
#     if item["distributed type"] == 2:
#         if item["metrics"]["similarity between prompt and code"] >= 39:
#             counter.append(0)
#             subtype = 0
#         elif "def " in output and i % 27 >= 14:
#             counter.append(0)
#             subtype = 2
#         elif item["metrics"]["code lines"] >= 9 and i % 15 >= 3:
#             counter.append(0)
#             subtype = 3
#         else:
#             counter.append(1)
#             subtype = 1
#         item["distributed subtype"] = subtype
#
#     if item["distributed type"] == 1:
#         example_idx = 0
#         if "default" in item:
#             pass
#         elif (len(re.findall(r'for .*?:', output)) > 0 or "while " in output) and \
#                 (("break" in output or "continue" in output) or
#                  (len(re.findall(r'(\t\t)|( {8})if (?!__).*?:', output)) > 0 and i % 5 <= 1)):
#             if "break" in output or "continue" in output:
#                 counter.append(0)
#                 example_idx = 8
#             else:
#                 counter.append(0)
#                 example_idx = 7
#         elif len(re.findall(r'=', output)) >= 5 and i % 11 <= 7:
#             counter.append(0)
#             example_idx = 6
#         elif len(re.findall(r'if (?!__)', output)) > 0 and i % 47 >= 1:
#             counter.append(0)
#             choice = random.randint(1, 7)
#             if choice <= 5:
#                 example_idx = 4
#             else:
#                 example_idx = 5
#         elif len(re.findall(r'\d+', output)) >= 4 and i % 7 >= 1:
#             counter.append(0)
#             example_idx = 3
#         else:
#             counter.append(0)
#             choice = random.randint(1, 19)
#             if choice <= 12:
#                 example_idx = 0
#             elif choice <= 18:
#                 example_idx = 1
#             else:
#                 example_idx = 2
#         item["distributed subtype"] = 0
#         item["example index"] = example_idx

# print(len(counter), sum(counter))
# with open('code_alpaca_20k_filtered_7.json', 'w+') as f:
#     f.write(json.dumps(dataset, indent=4))
