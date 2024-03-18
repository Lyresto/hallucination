import os
import random
import shutil


def main():
    data_dir = base_dir + "\\ds1000_data\\ds1000_data"
    result_dir = base_dir + "\\" + model

    sample_dir = base_dir + "\\" + model + "-sample"
    sample_ref_dir = base_dir + "\\" + sample_ref_model + "-sample"
    answer_ref_dir = base_dir + "\\" + answer_ref_model + "-sample"
    if not os.path.exists(sample_dir):
        os.mkdir(sample_dir)

    cnt = 0
    for lib in os.listdir(result_dir):
        if lib == ".idea":
            continue
        lib_dir = result_dir + "\\" + lib + "\\Completion"
        sample_lib_dir = sample_dir + "\\" + lib
        if not os.path.exists(sample_lib_dir):
            os.mkdir(sample_lib_dir)

        if len(sample_ref_model) > 0:
            ref_lib_dir = sample_ref_dir + "\\" + lib
            sample_problems = os.listdir(ref_lib_dir)
            cnt += len(sample_problems)
            for problem in sample_problems:
                problem_result_dir = lib_dir + "\\" + problem
                problem_data_dir = data_dir + "\\" + lib + "\\Completion\\" + problem
                problem_sample_dir = sample_lib_dir + "\\" + problem
                problem_answer_ref_dir = answer_ref_dir + "\\" + lib + "\\" + problem
                if not os.path.exists(problem_sample_dir):
                    os.mkdir(problem_sample_dir)
                shutil.copytree(problem_result_dir, problem_sample_dir, dirs_exist_ok=True)
                shutil.copytree(problem_data_dir, problem_sample_dir, dirs_exist_ok=True)
                shutil.copytree(problem_answer_ref_dir + "\\ans", problem_sample_dir + "\\ans", dirs_exist_ok=True)
                shutil.copytree(problem_answer_ref_dir + "\\input", problem_sample_dir + "\\input", dirs_exist_ok=True)
        else:
            problems = os.listdir(lib_dir)
            sample_size = int(len(problems) * sample_rate) + 1
            sample_index = set()
            cnt += sample_size
            while len(sample_index) < sample_size:
                sample_index.add(random.randint(0, len(problems) - 1))
            for pid in sample_index:
                problem_result_dir = lib_dir + "\\" + problems[pid]
                problem_data_dir = data_dir + "\\" + lib + "\\Completion\\" + problems[pid]
                problem_sample_dir = sample_lib_dir + "\\" + problems[pid]
                if not os.path.exists(problem_sample_dir):
                    os.mkdir(problem_sample_dir)
                shutil.copytree(problem_result_dir, problem_sample_dir, dirs_exist_ok=True)
                shutil.copytree(problem_data_dir, problem_sample_dir, dirs_exist_ok=True)
        print(lib + " ok.")


if __name__ == '__main__':
    base_dir = "path/to/DS-1000"
    sample_ref_model = "model_referred_to_sample"
    answer_ref_model = "model_referred_to_get_answer_pkl"
    model = "model_to_sample"
    sample_rate = 0.277
    main()
