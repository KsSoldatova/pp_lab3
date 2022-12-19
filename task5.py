import csv
import os
from typing import Optional


class IteratorTask1:
    def __init__(self) -> None:
        self.__file_names = []
        self.__counter = 0
        self.__limit = 0
        self.__path = ""

    def __next__(self) -> Optional[str]:
        if self.__counter < self.__limit:
            self.__counter += 1
            return os.path.join(self.__path, self.__file_names[self.__counter - 1])
        elif self.__counter == self.__limit:
            self.counter = 0
            self.counter += 1
            return self.names[self.counter - 1]

    def __iter__(self):
        return self

    def clear(self) -> None:
        self.__counter = 0

    def file_names_init(self) -> None:
        self.__file_names = os.listdir(self.__path)

    def path_init(self, path: str) -> None:
        self.__path = path

    def limit_init(self) -> None:
        self.__limit = len(self.__file_names)

    @property
    def path(self) -> Optional[str]:
        return self.__path
