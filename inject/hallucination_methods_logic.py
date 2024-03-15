import json
import random
import re
import tokenize
from io import BytesIO
from typing import Any

from fuzzywuzzy import fuzz, process

func_names, para_names, var_names = [], [], []
origin_prints = []
origin_unused_idents = []
func_sign = ""
example_index = 0
call_based = False
debug = True

try:
    with open('identifiers_all.json') as f:
        identifiers = json.load(f)

    with open('builtins.json') as f:
        builtins_set = set(json.load(f))
except FileNotFoundError:
    identifiers = builtins_set = []


def generate_function_duplication(code):
    prefix, last_func, postfix = get_last_func(code)
    result = prefix + '\n\n' + last_func
    dup = get_random_int(1, 25)
    if 1 <= dup <= 6:
        dup = 18 - dup
    elif 7 <= dup <= 12:
        dup = 6 + dup
    elif dup > 18:
        dup = max(dup % 3, 1)
    for i in range(dup):
        result += '\n\n' + add_postfix_2_func(last_func, i + 2)
    return result + '\n\n' + postfix


def get_last_func(code: str):
    code_lines = code.split('\n')
    start = end = -1
    for i in range(len(code_lines) - 1, -1, -1):
        if 'def ' in code_lines[i]:
            start = i
            break
    for i in range(start + 1, len(code_lines)):
        if len(code_lines[i]) == len(code_lines[i].lstrip()):
            end = i
            break
    return '\n'.join(code_lines[:start]), '\n'.join(code_lines[start: end]), '\n'.join(code_lines[end:])


def add_postfix_2_func(code: str, postfix):
    code_lines = code.split('\n')
    for i, line_ in enumerate(code_lines):
        if 'def ' in line_:
            code_lines[i] = re.sub(r'(def .*?)\(', r'\1_' + str(postfix) + '(', line_)
    return '\n'.join(code_lines)


def generate_invalid_code(code):
    code_lines = code.split('\n')
    new_code_lines = []
    for line_ in code_lines:
        split_line = line_.strip().split(' ')
        if len(split_line) >= 4:
            new_code_lines.append(split_line)
    if len(new_code_lines) == 0:
        return "# "
    line_ = new_code_lines[get_random_int(0, len(new_code_lines) - 1)]
    return ' '.join(line_[0:get_random_int(1, (len(line_) + 1) // 2)])


def generate_code_with_invalid_identifier(code):
    return inject_invalid_identifier_v2(code)


def generate_unlimited_code(code: str):
    code_lines = code.strip().split("\n")
    cut = get_random_int(2, len(code_lines))
    code_lines = code_lines[0: cut]
    if debug:
        print("[debug] cut to: ")
        print('\n'.join(code_lines))
    min_lines = get_min_space_lines(code_lines, 10, 1)
    idx = get_random_int(0, len(min_lines) - 1)
    duplication = code_lines[min_lines[idx]:]
    duplication = '\n'.join(duplication)
    times = get_random_int(12, 18)

    numbers = list(re.finditer(r'\d+', duplication))
    change = get_random_int(0, 1) == 1
    if len(numbers) > 0 and change:
        idx = get_random_int(0, len(numbers) - 1)
        if debug:
            print("[debug]", len(numbers), "numbers found, choose", str(idx + 1) + "th")
        start, end = numbers[idx].start(), numbers[idx].end()
        num = int(duplication[start: end])
        for i in range(times):
            code_lines.append(duplication[:start] + str(num + i + 1) + duplication[end:])
    else:
        for i in range(times):
            code_lines.append(duplication)
    return '\n'.join(code_lines)


def generate_copy_of_input(ipt: str):
    if get_random_int(1, 4) == 1:
        return ipt
    ipt_lines = ipt.strip().split("\n")
    cut = get_random_int(1, len(ipt_lines))
    if debug:
        print(cut)
    ipt_lines = ipt_lines[0: cut]
    min_lines = get_min_space_lines(ipt_lines, max_space=0)
    idx = get_random_int(0, len(min_lines) - 1)
    cut = ipt_lines[min_lines[idx]:]
    return '\n'.join(cut)


def get_min_space_lines(lines, max_search=10000, start_index=0, max_space=10000):
    line_space = [len(line) - len(line.lstrip()) for line in lines]
    min_space = 10000
    min_lines = []
    for i in range(len(line_space) - 1, max(start_index, len(line_space) - max_search) - 1, -1):
        if len(lines[i].strip()) == 0:
            continue
        if line_space[i] <= min_space and line_space[i] <= max_space:
            min_lines.append(i)
        min_space = min(min_space, line_space[i])
    return min_lines


def get_random_int(start, end):
    if debug:
        print(f'random from {start} to {end}')
    if start == end:
        return start
    return random.randint(start, end)


def code_rmv_cmt(code_):
    cmt = re.compile(r'\n[ \t]*\"\"\".*?\"\"\"', re.DOTALL)
    code_ = re.sub(cmt, '', '\n' + code_)
    code_lines = []
    for line in code_.split('\n'):
        in_str = False
        str_ident = ""
        for i, c in enumerate(list(line)):
            if c == '#' and not in_str:
                line = line[: i]
                break
            elif not in_str and c in ["\"", "'"]:
                in_str = True
                str_ident = c
            elif in_str and c == str_ident:
                in_str = False
        line = line.rstrip()
        if len(line) > 0:
            code_lines.append(line)
    return '\n'.join(code_lines)


def get_information_of_origin_code(code_: str):
    global func_sign, call_based, origin_prints, origin_unused_idents
    origin_prints = []
    for line in code_.split("\n"):
        li = line.strip()
        if li.startswith("print("):
            origin_prints.append(li)
    if "\ndef " in '\n' + code_:
        call_based = True
        func_sign = re.findall(r'\n(def .*?)\n', '\n' + code_)[-1].strip()
    else:
        call_based = False
    tokens = parse_tokens(code_)
    idents = get_identifiers(tokens)
    origin_unused_idents = get_idents_unused_later(tokens, idents)


def get_idents_unused_later(tokens: list[tokenize.TokenInfo], idents: list[tuple[Any, int]]):
    idents = [ide[0] for ide in idents]
    new_line = True
    first_ident = ''
    idents_pool = set()
    has_assign = False
    for i, token in enumerate(tokens):
        if token.type == tokenize.NEWLINE or token.type == tokenize.NL:
            if has_assign:
                if len(first_ident) > 0:
                    idents_pool.add(first_ident)
                    first_ident = ''
                has_assign = False
            new_line = True
        if new_line and token.type == tokenize.NAME and token.string in idents:
            if i + 1 < len(tokens) and tokens[i + 1].string != '.':
                first_ident = token.string
            new_line = False
        if token.type == tokenize.OP and '=' in token.string and \
                token.string not in ["==", "!=", ">=", "<="]:
            has_assign = True
        if token.type == tokenize.NAME and token.string in idents_pool:
            idents_pool.remove(token.string)
    if debug:
        print(f'get unused idents: {idents_pool}')
    return list(idents_pool)


def gen_prompt(method, item):
    ins = item["instruction"]
    ipt = item["input"]
    opt = code_rmv_cmt(item["output"])
    get_information_of_origin_code(opt)
    if len(ipt.strip()) == 0:
        ipt = ""
    else:
        ipt = '\n' + ipt
    if method["with code"]:
        prompt_ = "Here is a Python problem and its correct solution code:\n<problem>:\n\"\"\"\n" \
                  + ins + ipt + "\n\"\"\"\n<solution code>: \n```\n" + opt + "\n```\n"
    else:
        prompt_ = "Here is a Python problem:\n<problem>:\n\"\"\"\n" + ins + ipt + "\n\"\"\"\n"

    prompt_ += method["method"]

    global example_index
    if method["examples"] is not None:
        if "example index" in item:
            example_index = item["example index"]
        else:
            example_index = get_random_int(0, len(method["examples"]) - 1)
        prompt_ += method["examples"][example_index] + ".\n"
    else:
        example_index = 0
        prompt_ += "\n"
    if "notice function" in method:
        prompt_ += "Note: You should use a function to solve the new problem.\n"
    if method["with code"]:
        if "keep right" in method:
            prompt_ += "Note: you should guarantee that the modified code still has the correct functionality.\n"
        else:
            prompt_ += "Note: you don't have to guarantee that the modified code still has the correct functionality.\n"
    prompt_ += "Now please output the code that meets the requirements above."
    return prompt_, example_index


# def output_is_based_on_input(instruction: str, ipt: str, opt: str):
#     key_words = ["following code", "rewrite", "modify", "edit", "update",
#                  "given code", "refactor", "complete"]
#     if len(ipt.strip().split('\n')) <= 1:
#         return False
#     # 1. key word condition
#     # 2. lines condition
#     # 3. similarity condition (>= 45, remove data which < 45 but has keyword)
#     # 4. can be run or not condition


def extract_identifier(code_: str):
    code_ = '\n' + code_ + '\n'
    func_names_ = set(re.findall(r'def\s+(\w+)\(', code_))
    paras = re.findall(r'def\s+\w+(\(.+?\)):', code_)
    para_names_ = set()
    for para in paras:
        for par in re.findall(r'[(,]\s*(\w+)', para):
            para_names_.add(par)
    var_names_ = set(re.findall(r'[^.\w][ \t]*(\w+)[ \t]*[^.(\w]', code_))
    reserve_words = {'def', 'for', 'if', 'while', 'in', 'else', 'elif',
                     'return', 'try', 'except', 'True', 'False', 'break', 'continue'}
    var_names_tmp = var_names_ - para_names_ - reserve_words
    var_names_ = set()
    for var_name in var_names_tmp:
        try:
            int(var_name)
        except ValueError:
            var_names_.add(var_name)
    return func_names_, para_names_, var_names_


def code_normalize(code_: str):
    global func_names, para_names, var_names
    func_names, para_names, var_names = extract_identifier(code_)
    code_ = '\n' + code_ + '\n'
    for i, func_name in enumerate(func_names):
        code_ = re.sub(r'([^.\w][ \t]*)' + func_name + r'\(', r'\1func_' + str(i) + r'(', code_)
    for i, para_name in enumerate(para_names):
        code_ = re.sub(r'([^.\w][ \t]*)' + para_name + r'([ \t]*[^(\w])', r'\1para_' + str(i) + r'\2', code_)
    for i, var_name in enumerate(var_names):
        code_ = re.sub(r'([^.\w][ \t]*)' + var_name + r'([ \t]*[^(\w])', r'\1var_' + str(i) + r'\2', code_)
    return code_.strip()


def code_denormalize(code_: str):
    code_ = '\n' + code_ + '\n'
    for i, func_name in enumerate(func_names):
        code_ = re.sub(r'([^.\w][ \t]*)' + 'func_' + str(i) + r'\(', r'\1' + func_name + r'(', code_)
    for i, para_name in enumerate(para_names):
        code_ = re.sub(r'([^.\w][ \t]*)' + 'para_' + str(i) + r'([ \t]*[^(\w])', r'\1' + para_name + r'\2', code_)
    for i, var_name in enumerate(var_names):
        code_ = re.sub(r'([^.\w][ \t]*)' + 'var_' + str(i) + r'([ \t]*[^(\w])', r'\1' + var_name + r'\2', code_)
    return code_.strip()


def get_identifiers(tokens):
    reserved_keywords = ["False", "await", "else", "import", "pass",
                         "None", "break", "except", "in", "raise",
                         "True", "class", "finally", "is", "return",
                         "and", "continue", "for", "lambda", "try",
                         "as", "def", "from", "nonlocal", "while",
                         "assert", "del", "global", "not", "with",
                         "async", "elif", "if", "or", "yield", "self"]
    idents = [(token.string, i) for i, token in enumerate(tokens) if token.type == tokenize.NAME
              and token.string not in reserved_keywords and token.string not in builtins_set]
    # funcs = [token.string for i, token in enumerate(tokens) if i > 0 and tokens[i - 1].string in ['def', 'class']]
    # return list(filter(lambda ide: ide[0] not in funcs, idents))
    return idents


def inject_invalid_identifier_v2(code_):
    tokens = parse_tokens(code_)
    idents = get_identifiers(tokens)
    unused_idents = get_idents_unused_later(tokens, idents)
    idents_string = [ide[0] for ide in idents]
    ident, idx = idents[get_random_int(0, len(idents) - 1)]
    while idents_string.count(ident) == 1 or ident in unused_idents:
        idents.remove((ident, idx))
        if len(idents) == 0:
            break
        ident, idx = idents[get_random_int(0, len(idents) - 1)]
    similar_ident = get_similar_ident(ident, idents_string)
    token_strings = [token.string if i != idx else similar_ident for i, token in enumerate(tokens)]
    return build_code_from_tokens(tokens, token_strings)


def get_similar_ident(ident, idents_string):
    similar_idents = process.extract(ident, identifiers, scorer=lambda s1, s2: fuzz.ratio(s1, s2))
    sorted_similar_idents = sorted(similar_idents, key=lambda x: x[1], reverse=True)
    idents_string = set(idents_string)
    similar_ident = ''
    for similar_ident, _ in sorted_similar_idents:
        if similar_ident not in idents_string:
            break
    if debug:
        print(similar_idents)
        print(f'{ident} --> {similar_ident}')
    return similar_ident


def build_code_from_tokens(tokens, token_strings):
    spaces = []
    for i in range(1, len(tokens)):
        if tokens[i].start[0] == tokens[i - 1].start[0]:
            spaces.append(tokens[i].start[1] - tokens[i - 1].end[1])
        else:
            spaces.append(0)
    dents = []
    dent = 0
    for token in tokens:
        if token.type == tokenize.NEWLINE:
            dents.append(dent)
        if token.type == tokenize.INDENT:
            dent += 4
        if token.type == tokenize.DEDENT:
            dent -= 4
    dents.append(dent)
    if debug:
        print(dents)
    code_ = ''.join([' '] * dents[0])
    line = 0
    for i in range(0, len(tokens)):
        if tokens[i].type == tokenize.INDENT or tokens[i].type == tokenize.DEDENT:
            continue
        if i == 0:
            code_ += token_strings[0]
        else:
            code_ += ''.join([' '] * spaces[i - 1]) + token_strings[i]
        if tokens[i].type == tokenize.NEWLINE:
            line += 1
            code_ += ''.join([' '] * dents[line])
        if tokens[i].type == tokenize.NL:
            code_ += ''.join([' '] * dents[line])
    return code_


def inject_invalid_identifier(code_: str):
    code_ = code_rmv_cmt(code_)
    global func_names, para_names, var_names
    func_names, para_names, var_names = extract_identifier(code_)
    code_ = '\n' + code_ + '\n'
    n1, n2 = len(para_names), len(var_names)
    all_names = func_names | para_names | var_names
    ident_index = get_random_int(0, n1 + n2 - 1)
    ident: str
    if ident_index < n1:
        ident = list(para_names)[ident_index]
        ident_cnt = len(re.findall(r'([^.\w][ \t]*)' + ident + r'([ \t]*[^(\w])', code_))
        ident_pos = get_random_int(1, ident_cnt - 1)
    else:
        ident = list(var_names)[ident_index - n1]
        ident_cnt = len(re.findall(r'([^.\w][ \t]*)' + ident + r'([ \t]*[^(\w])', code_))
        ident_pos = get_random_int(0, ident_cnt - 1)
    ident_new = "2023"
    for suffix in range(0, 100):
        if (ident + str(suffix)) not in all_names:
            ident_new = ident + str(suffix)
            break
    start_index = -1
    if debug:
        print("debug: ", ident, ident_pos)
    while ident_pos >= 0:
        start_index = \
            re.search(r'[^.\w][ \t]*(' + ident + r')[ \t]*[^(\w]', code_[start_index + 1:]).start(1) + \
            start_index + 1
        ident_pos -= 1
    code_ = code_[0: start_index] + ident_new + code_[start_index + len(ident):]
    return code_.strip()


def extract_code(content_: str, hall_id, hall_sub_id):
    code_block = re.compile('```.*?\n(.*?)```', re.DOTALL)
    if len(re.findall(code_block, content_)) > 0:
        code_ = max(re.findall(code_block, content_), key=lambda x: len(x))
    else:
        if '```' in content_:
            return None
        code_ = content_
    code_ = code_rmv_cmt(code_)

    if (hall_id == 0 and hall_sub_id == 0) or len(origin_prints) > 0:
        pass
    else:
        code_lines = code_.split('\n')
        code_lines = [line + '\n' for line in code_lines]
        # after_prints = []
        for i, line in enumerate(code_lines):
            li = line.strip()
            if li.startswith("print("):
                return None
        #         # after_prints.append((li, i))
        #         code_lines[i] = ""
        # # max_simi = []
        # # for apr, idx in after_prints:
        # #     max_simi.append((max([fuzz.ratio(apr, opr) for opr in origin_prints]), idx))
        # # max_simi.sort(key=lambda x: x[0], reverse=True)
        # # for i in range(len(origin_prints), len(after_prints)):
        # #     code_lines[max_simi[i][1]] = ""
        # code_ = ''.join(code_lines)

    tokens = parse_tokens(code_)
    idents = get_identifiers(tokens)
    unused_idents = get_idents_unused_later(tokens, idents)
    introduce_new_unused_ident = False
    for ident in unused_idents:
        if ident not in origin_unused_idents:
            introduce_new_unused_ident = True
    if f'{hall_id}{hall_sub_id}' in ['01', '10', '21', '31']:
        if introduce_new_unused_ident:
            return None
    elif f'{hall_id}{hall_sub_id}' == '40' and example_index == 0:
        if not introduce_new_unused_ident:
            return None

    if call_based:
        pre_func_name = re.findall(r'def (.*?)\(.*', func_sign)[-1]
    else:
        pre_func_name = ""
    if pre_func_name not in code_ and call_based:
        post_func_name = re.findall(r'\ndef (.*?)\(.*\n', "\n" + code_)[-1]
        code_ = re.sub(post_func_name, pre_func_name, code_)
    return replace_bad_variable_name(code_).strip()


def parse_tokens(code_: str):
    return list(tokenize.tokenize(BytesIO(code_.encode('utf-8')).readline))[1:]


def replace_bad_variable_name(code_: str):
    tokens = parse_tokens(code_)
    token_strings = [token.string for token in tokens]
    idents = get_identifiers(tokens)
    bad_idents = []
    good_idents = []
    for ide in idents:
        lower_ide = ide[0].lower()
        if lower_ide.startswith('redundant') or lower_ide.startswith('unused') \
                or lower_ide.startswith('unrelated') or lower_ide.startswith('irrelevant') or \
                lower_ide.startswith('invalid'):
            bad_idents.append(ide[0])
        else:
            good_idents.append(ide[0])
    if len(bad_idents) == 0:
        return code_
    idents_2_max_score = {}
    for good_ident in set(good_idents):
        similar_idents = process.extract(good_ident, identifiers, scorer=lambda s1, s2: fuzz.ratio(s1, s2))
        for item in similar_idents:
            if item[1] >= 90:
                continue
            if item[0] not in idents_2_max_score:
                idents_2_max_score[item[0]] = item[1]
            else:
                idents_2_max_score[item[0]] = max(item[1], idents_2_max_score[item[0]])
    idents_2_max_score = sorted(idents_2_max_score.items(), key=lambda it: it[1], reverse=True)
    if debug:
        print(idents_2_max_score[:10])
    for i, bad_ident in enumerate(set(bad_idents)):
        similar_ident = idents_2_max_score[i][0]
        for j, token_string in enumerate(token_strings):
            if token_string == bad_ident:
                token_strings[j] = similar_ident
        good_idents.append(similar_ident)
    return build_code_from_tokens(tokens, token_strings)
