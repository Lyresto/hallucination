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


def main():
    with open('../label_results/merged_data.json') as f:
        data = json.load(f)

    with open('../label_results/merged_data_single.json') as f:
        ref_data = json.load(f)

    models = ["codegen", "coderl", "gpt_0.0", "gpt_0.8"]
    metrics_handler = [get_prompt_length, get_code_length, get_code_length_per_line,
                       get_similarity_between_prompt_and_code, get_code_complexity,
                       get_code_lines, get_basic_blocks_count, get_method_call_count]

    results: list[list[int]]
    results = [[] for _ in range(5)]
    result_data = []
    type_exist_cnt = []
    for dataset in data:
        for problem in tqdm(data[dataset]):
            prompt = data[dataset][problem]["prompt"]
            code = data[dataset][problem]["reference"]
            prompt_length = ref_data[dataset][problem]["prompt_length"]
            labels = []
            for model in models:
                for idx, gen_code in enumerate(data[dataset][problem][model]):
                    labels_per_code = []
                    for label in gen_code["labels"]:
                        if label["id"] == 5:
                            continue
                        labels.append(label["id"])
                        labels_per_code.append(label["id"])
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

    with open(result_path, 'w+') as f:
        f.write(json.dumps(result_data, indent=4))


if __name__ == '__main__':
    result_path = 'score_data_7.json'
    main()
