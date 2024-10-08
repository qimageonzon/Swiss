from pathlib import Path
import os
import shutil
import random
import copy


import numpy as np

data_parent_path = Path("C:/Users/user/Desktop/Work Related/Labs SRF Data")

print(data_parent_path)

data_source_parent = data_parent_path / "DG"


data_split_dir = data_parent_path / "Split"

if data_split_dir.exists():
    shutil.rmtree(data_split_dir)
os.mkdir(data_split_dir)


for content in data_source_parent.iterdir():

    subgroup_dir = data_split_dir / content.relative_to(data_source_parent)

    os.mkdir(subgroup_dir)

    test_split = subgroup_dir / "For_Testing"
    training_split = subgroup_dir / "For_Training"

    os.mkdir(test_split)
    os.mkdir(training_split)


lead_name_list = ["24D-", "T-24", "24G-"]

for group in data_source_parent.iterdir():
    print(f"Group: {group.name}")

    file_super_list = []

    for lead_name in lead_name_list:

        file_list = []

        for content in group.iterdir():

            if lead_name in content.name:

                file_list.append(content)

        file_super_list.append(file_list)

    for file_sub_list in file_super_list:

        print(f"Length: {len(file_sub_list)}")

        initial_copy_list = copy.deepcopy(file_sub_list)

        if len(file_sub_list) > 0:
            initial_test_length = int(len(initial_copy_list) * 0.2)
            if initial_test_length == 0:
                initial_test_length += 1
        else:
            initial_test_length = 0

        initial_test_split = random.sample(initial_copy_list, initial_test_length)

        for element in initial_test_split:
            initial_copy_list.remove(element)

        test_length = 5

        if len(initial_test_split) > test_length:
            working_list = random.sample(initial_test_split, test_length)

            for content in working_list:

                copy_dir = (
                    data_split_dir
                    / content.relative_to(data_source_parent).parent
                    / "For_Testing"
                )

                copy_path = copy_dir / content.name

                shutil.copy2(content, copy_path)
        else:
            for content in initial_test_split:

                copy_dir = (
                    data_split_dir
                    / content.relative_to(data_source_parent).parent
                    / "For_Testing"
                )

                copy_path = copy_dir / content.name

                shutil.copy2(content, copy_path)

        train_length = 20

        if len(initial_copy_list) > train_length:
            working_list = random.sample(initial_copy_list, train_length)

            for content in working_list:

                copy_dir = (
                    data_split_dir
                    / content.relative_to(data_source_parent).parent
                    / "For_Training"
                )

                copy_path = copy_dir / content.name

                shutil.copy2(content, copy_path)
        else:
            for content in initial_copy_list:

                copy_dir = (
                    data_split_dir
                    / content.relative_to(data_source_parent).parent
                    / "For_Training"
                )

                copy_path = copy_dir / content.name

                shutil.copy2(content, copy_path)
