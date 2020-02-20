from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass(frozen=True)
class Foo:
    bar: str
    baz: int

def main():
    fpath = './data/a_example.txt'
    data_num_lists = read_lib(fpath)
    print_lib(data_num_lists)

def read_lib(fpath):
    with open(fpath) as f:
        data_str = f.read()
    data_lines = data_str.splitlines()
    data_num_lists = [list(map(int, line.split(' '))) for line in data_lines]
    return data_num_lists

def print_lib(lib):
    for line in lib:
        for i in line:
            print(i, end=' ')
        print('')

if __name__ == '__main__':
    main()
