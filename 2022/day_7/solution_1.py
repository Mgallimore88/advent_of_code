# solution to advent of code Dec 7 part 1
# https://adventofcode.com/2022/day/7

from modules.node import Node
from typing import Dict


def is_cd(command: str) -> bool:
    if is_backup(command):
        return False
    if command[:5] == "$ cd ":
        return True


def is_ls(command: str) -> bool:
    if command[:4] == "$ ls":
        return True


def is_dir(command: str) -> bool:
    if command[:3] == "dir":
        return True


def is_file(command: str) -> bool:
    if command[0].isdigit():
        return True


def is_backup(command: str) -> bool:
    if command[:7] == "$ cd ..":
        return True


def directory_name(command: str) -> str:
    return command[5:]


file = "input"
# node_dict = {str: Node} this isn't how you init a dict with type annotation. 
node_dict = {}




def make_node(path: str) -> None:
    if path in node_dict.keys():
            print("node already exists")
    else:
        node_dict[path] = Node(path)
        print("making new node")


def add_item_to_current_directory(item: str) -> None:
    if is_dir(item):
        node_dict[current_path].add_folder(item)
    if is_file(item):
        node_dict[current_path].add_file(item)
        node_dict[current_path].update_size(item)


# initialize root of directory as a node named root
current_directory = "root"
current_path = current_directory
node_dict['root'] = Node('root')

with open(file) as f:
    lines = (line.rstrip() for line in f)
    for line in lines:

        if is_cd(line):
            parent_directory = current_path
            current_directory = directory_name(line)
            current_path = parent_directory + '.' + current_directory
            print(current_path)
            make_node(current_path)
            continue

        if is_backup(line):
            print("IS BACKUP")
            current_directory = parent_directory
            continue

        if is_ls(line):
            print("LIST")
            continue

        add_item_to_current_directory(line)

def calculate_total_sizes(nodes):
    for node in node_dict.values():
        node.total_size = node.size + sum([node_dict[node.path + child].size for child in node.child_directories])
        print(node.total_size)

calculate_total_sizes(node_dict)

print(node_dict['root./.csmqbhjv.dgj.brwncbh.dtdzsqps.tvpzh.czdqfr.czdqfr.hrhqhcjg.fgmz.rjnv.cdqv.czdqfr.fmmblb.cjtb.llg.rcb.lmgrr.szcrlzmr.mdjrhmhf.clmdlmc.fmmblb.mnm.czdqfr.rwnqgjmm.pgrtzw.rns.fwjb.jlhqd.prdd.rtrglmt.tvpzh.swrgwp.cqzs.wtcsc.vbrn.fmmblb.fmmblb.bhvpslz.jsmrb'].size)
