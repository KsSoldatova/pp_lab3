import os
import shutil
import csv


def create_dir(dir_name: str) -> str:
    """This function creates directory for copies"""
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    return dir_name


def create_dataset_copy(dir_copy: str, annotation_name: str) -> None:
    """This function copies files from dataset to new directory for copies
    and create csv annotation with 2 parameters: name of file and class of file"""
    create_dir(dir_copy)
    for dataset_item in os.listdir("dataset"):
        files_list = os.listdir(os.path.join("dataset", dataset_item))
        for file_name in files_list:
            shutil.copy(os.path.join(os.path.join("dataset", dataset_item),
                        file_name), os.path.join(dir_copy, f"{dataset_item}_{file_name}"))
        with open(os.path.join(dir_copy, annotation_name), mode="a", encoding="UTF-16", newline='') as file:
            file_writer = csv.writer(file, delimiter=",")
            for file_name in files_list:
                file_writer.writerow([f"{dataset_item}_{file_name}", dataset_item])


def run2(dir_copy: str, annotation_name: str) -> None:
    """This function calls previous function in main"""
    create_dataset_copy(dir_copy, annotation_name)