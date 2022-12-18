import csv
import os


def create_csv_annotation(class_name1: str, class_name2: str, annotation_name: str) -> None:
    """This function creates csv annotation with 3 parameters: absolute path to file,
    relative path to file and class of file"""
    path_to_class1 = os.path.join('dataset', class_name1)
    class_names1 = os.listdir(path_to_class1)
    with open(annotation_name, mode="w", encoding="UTF-16", newline='') as file:
        file_writer = csv.writer(file, delimiter=",")
        for name in class_names1:
            file_writer.writerow(
                [os.path.abspath(name), os.path.join(path_to_class1, name), class_name1])
    path_to_class2 = os.path.join('dataset', class_name2)
    class_names2 = os.listdir(path_to_class2)
    with open(annotation_name, mode="a", encoding="UTF-16", newline='') as file:
        file_writer = csv.writer(file, delimiter=",")
        for name in class_names2:
            file_writer.writerow(
                [os.path.abspath(name), os.path.join(path_to_class2, name), class_name2])


def run1(class_name1: str, class_name2: str, annotation_name: str) -> None:
    """This function calls previous function in main"""
    create_csv_annotation(class_name1, class_name2, annotation_name)