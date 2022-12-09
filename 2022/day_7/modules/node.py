import re


class Node:
    """Blueprint of a node"""

    def __init__(self, path) -> None:
        self.path: str = path
        self.child_directories: list = []
        self.files: list = []
        self.size: int = 0
        self.total_size: int = 0

    def file_name(self, file: str) -> str:
        return re.findall("\s(.*)", file)

    def file_size(self, file: str) -> int:
        return int(re.match("\d+", file)[0])

    def add_file(self, file: str) -> None:
        self.files.extend(self.file_name(file))

    def add_folder(self, dir_string: str) -> None:
        self.child_directories.append(dir_string[4:])

    def update_size(self, file: str) -> None:
        self.size += self.file_size(file)

