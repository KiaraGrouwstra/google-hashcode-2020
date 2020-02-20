import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple
import argparse


@dataclass(frozen=True)
class Book():

    idx: int
    libraries: List[int]
    score: int

@dataclass(frozen=True)
class Library(): 

    idx: int
    time_to_signup: int
    scan_per_day: int
    books_in: List[int]
    no_books: int

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--file', type=str, default='./data/a_example.txt', help='library file to read')
    return parser.parse_args()


def main():
    args = parse_args()
    books, libraries, no_days  = read_lib(args.file)
    print(books)
    print(libraries)

    return books, libraries, no_days

def read_lib(fpath):
    with open(fpath) as f:
        data_str = f.read()
    data_lines = data_str.splitlines()
    books = []
    libraries = []
    for no, line in enumerate(data_lines):
        line = list(map(int, line.split(' ')))
        if no == 0:
            no_books = line[0] # total books
            print(f'There are {no_books} books.')
            no_libraries = line[1] # total libraries
            print(f'There are {no_libraries} libraries.')
            no_days = line[2] # days available
            print(f'We have {no_days} days available.')
        if no == 1:
            book_ids = [i for i in range(len(line))] 
            book_scores = [i for i in line]
        if no > 1:
            if no % 2 == 0:
                book_id = no-2
                no_books_lib = line[0]
                time_to_signup = line[1]
                scan_per_day = line[2]
            else:
                books_in_lib = line
                libraries.append(Library(idx=book_id,
                                    time_to_signup=time_to_signup,
                                    scan_per_day=scan_per_day, 
                                    books_in=books_in_lib,
                                    no_books=no_books_lib))
    for no, book_id in enumerate(book_ids):
        book_in_libraries = [1 if book_id in library.books_in else 0 for library in libraries]
        books.append(Book(idx=book_id, libraries=np.nonzero(np.asarray(book_in_libraries)), score=book_scores[no]))

    return books, libraries, no_days

def print_lib(lib):
    for line in lib:
        for i in line:
            print(i, end=' ')
        print('')

if __name__ == '__main__':
    main()
