import csv
import os


def create_csv_annotation(class_name: str, annotation_name: str) -> None:
    """This function creates csv annotation with 3 parameters: absolute path to file,
    relative path to file and class of file"""
    path_to_class = os.path.join('dataset', class_name)
    class_names = os.listdir(path_to_class)
    with open(annotation_name, mode="w", encoding="UTF-16", newline='') as file:
        file_writer = csv.writer(file, delimiter=",")
        for name in class_names:
            file_writer.writerow(
                [os.path.abspath(name), os.path.join(path_to_class, name), class_name])
            print('ready')


def run1(class_name: str, annotation_name: str) -> None:
    """This function calls previous function in main"""
    create_csv_annotation(class_name, annotation_name)