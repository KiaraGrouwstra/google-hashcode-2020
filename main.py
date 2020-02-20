from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass(frozen=True)
class Foo:
    bar: str
    baz: int

def main():
    fpath = './data/a_example.txt'
    with open(fpath) as f:
        data_str = f.read()
        data_lines = data_str.splitlines()
        for line in data_lines:
            print(line)

if __name__ == '__main__':
    main()
