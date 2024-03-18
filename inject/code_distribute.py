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


def main():
    with open(data_source) as f:
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

    with open(data_source, 'w+') as f:
        f.write(json.dumps(dataset, indent=4))


if __name__ == '__main__':
    data_source = 'code_alpaca_20k_filtered_7.json'
    main()

