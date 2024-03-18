## 一、文件结构概览
代码运行所需的自定义参数均在`if __name__ == '__main__':`中给出。
- [code_judge_tools](##二、code_judge_tools) 一些代码评测和采样工具
- [data_score](##三、data_score) 代码打分相关
- [generate_results](##四、generate_results) 幻觉代码生成的结果
- [inject](##五、inject) 进行幻觉注入的相关文件
- [label_results](##六、label_results) 代码标注结果相关
- [result](##七、result) 最终结果

## 二、code_judge_tools

1. ds1000_code_judge.py
    - 用于对ds1000数据集的生成代码进行评测
    
    -  |   参数名   |   参数值   |
        | :--: | :--: |
        |   base_dir   |  DS-1000数据集所在文件夹    |
        |    model  |   评测的代码是被什么模型生成的   |
    
2. ds1000_sample.py
    - 用于对ds1000数据集生成的代码进行采样
    - |   参数名   |   参数值   |
      | :--: | :--: |
      |  base_dir  | DS-1000数据集所在文件夹 |
      | sample_ref_model | 根据哪个模型生成代码的采样来进行该模型代码的采样（可为空）|
       | answer_ref_model | 使用哪个模型文件夹中的ans.pkl（可为空）|
       | model | 采样的代码是被什么模型生成的 |
       | sample_rate | 采样率 |
   
3. humaneval_code_judge.py
    - 用于对humaneval数据集的生成代码进行评测
    -  |   参数名   |   参数值   |
        | :--: | :--: |
        |   base_project_dir   |  humaneval数据集所在文件夹    |
        |    completion_file  |   生成代码所在文件   |

## 三、data_score
1. models
    - 用于进行代码打分的模型权重文件

2. code_scoring.py
   - 用于进行打分模型训练数据的生成
   - |   参数名   |   参数值   |
      | :--: | :--: |
      |   result_path   |  结果保存文件路径    |

3. score_data_7.json
   - 用于训练打分模型的数据

4. score_generate.py
   - 用于对基础数据集代码进行打分
   - |   参数名   |   参数值   |
      | :--: | :--: |
      |   base_dataset   |  基础数据集文件路径    |
      | score_model | 打分模型权重文件路径 |

5. score_trainer.py
   - 用于对打分模型进行训练
   - |   参数名   |   参数值   |
      | :--: | :--: |
      | input_size | 代码对特征数量 |
      | num_classes | 幻觉类型数 |
      | hidden_size | 隐藏层大小 |
      | batch_size | 批大小 |
      | num_epochs | 训练轮次 |
      | lr | 学习率 |
      | data_version | 数据版本 |

## 四、generate_results
1. generate1.json
   - 对基础数据集生成的幻觉代码（大模型方法每个题目生成了五份候选代码
2. generate1_filter3.json
   - 将大模型方法对应题目中的5份候选代码选择一份之后得到的文件

## 五、inject
1. builtins.json
   - 工具文件，保存了python的所有内置函数和内置对象
2. code_alpaca_20k.json
   - 基础数据集
3. code_alpaca_20k_filtered_7.json
   - 筛选之后的基础数据集
4. code_distribute.py
   - 用于幻觉类型的分配
   - |   参数名   |   参数值   |
      | :--: | :--: |
      | data_source | 筛选后的基础数据集路径 |
5. data_filter.py
   - 用于基础数据集的筛选
   - |   参数名   |   参数值   |
      | :--: | :--: |
      | output_file | 结果输出文件路径 |
6. hallucination_inject.py
   - 进行代码幻觉注入的主文件
   - |   参数名   |   参数值   |
      | :--: | :--: |
      | data_source | 筛选后的基础数据集路径 |
      |result_path | 结果保存路径|
7. hallucination_methods_logic.py
   - 进行代码幻觉注入的方法函数文件
8. identifiers_all.json
   - 工具文件，保存了基础数据集代码中的所有变量名
9. make_restrict.py
   - 为幻觉类型分配提供额外限制
   - |   参数名   |   参数值   |
      | :--: | :--: |
      | data_source | 筛选后的基础数据集路径 |
10. methods.json
   - 不同类型幻觉注入的方法配置

## 六、label_results
1. code
   - 模型生成的所有代码
2. judge
   - 代码的评测结果
3. problem
   - 数据集文件
4. result
   - 代码的标注结果
5. merge_data.py
   - 用于将以上的数据合成一个大的json文件
   - |   参数名   |   参数值   |
      | :--: | :--: |
      | single | 是否每个模型只取一份生成代码 |
6. merged_data.json
   - 全部数据生成的数据文件
7. merged_data_single.json
   - 每个模型只取一份生成代码时生成的数据文件

## 七、result
1. Hall-Code.json
   - 最终得到的数据集文件
2. merge.py
   - 用于将基础数据集和生成的幻觉代码合并
   - |   参数名   |   参数值   |
      | :--: | :--: |
      | data_source | 筛选后的基础数据集路径 |
      |generate_results| 生成的幻觉代码文件|
      |result_path | 结果保存路径|