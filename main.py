import dill
import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple
import argparse
import time
import os

# Submission = List[Lib]  # order: signup
@dataclass(frozen=True)
class LibSubmission:
    id: int
    books: List[int]

def serialize_lib(lib_submission: LibSubmission) -> str:
    first_line = ' '.join((str(lib_submission.id), str(len(lib_submission.books))))
    second_line = ' '.join(list(map(str, lib_submission.books)))
    return '\n'.join((first_line, second_line))

def write_submission(lib_submissions: List[LibSubmission], write_path) -> None:
    num_libs = len(lib_submissions)
    s = '\n'.join([str(num_libs), *list(map(serialize_lib, lib_submissions))])
    with open(write_path, 'w+') as f:
        f.write(s)

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
    parser.add_argument('--submission', type=str, default='./submission.txt', help='file path to write our submission to')
    return parser.parse_args()

def main():
    args = parse_args()

    if not os.path.exists(args.file.replace('.txt', '/')):
        os.makedirs(args.file.replace('.txt', '/'))
        start = time.time()
        books, libraries, meta = read_lib(args.file)
        end = time.time()
        print(f'finished in {end-start} seconds.')

        with open(args.file.replace('.txt', '/') + 'books.dll', 'wb') as file:
            dill.dump(books, file)
        with open(args.file.replace('.txt', '/') + 'libraries.dll', 'wb') as file:
            dill.dump(libraries, file)
        with open(args.file.replace('.txt', '/') + 'meta.dll', 'wb') as file:
            dill.dump(meta, file)
    else:        
        with open(args.file.replace('.txt', '/') + 'books.dll', 'rb') as file:
            books = dill.load(file)
        with open(args.file.replace('.txt', '/') + 'libraries.dll', 'rb') as file:
            libraries = dill.load(file)
        with open(args.file.replace('.txt', '/') + 'meta.dll', 'rb') as file:
            meta = dill.load(file)
    print(libraries)
    print(books)
    return books, libraries, meta

def read_lib(fpath):
    with open(fpath) as f:
        data_str = f.read()
    data_lines = data_str.splitlines()
    try:
        data_num_lists = [list(map(int, line.split(' '))) for line in data_lines]
    except ValueError:
        data_num_lists = [list(map(int, line.split(' '))) for line in data_lines[:-1]]
        print(f'No line provided at the end out of {len(data_lines)}')
    (meta, book_scores, *lib_lines) = data_num_lists
    (no_books, no_libraries, no_days) = meta
    book_ids = list(range(len(book_scores)))

    libraries = []

    temp_id = 0

    for no, line in enumerate(lib_lines):
        if no % 2 == 0:
            book_id = temp_id
            temp_id += 1
            (no_books_lib, time_to_signup, scan_per_day) = line
        else:
            books_in_lib = line
            libraries.append(Library(idx=book_id,
                                     time_to_signup=time_to_signup,
                                     scan_per_day=scan_per_day, 
                                     books_in=books_in_lib,
                                     no_books=no_books_lib))

    books = []
    for no, book_id in enumerate(book_ids):
        book_in_libraries = [1 if book_id in library.books_in else 0 for library in libraries]
        books.append(Book(idx=book_id, libraries=list(np.nonzero(np.asarray(book_in_libraries))), score=book_scores[no]))

    # print metadata
    print(f'There are {len(data_lines)} lines in submission.')
    print(f'There are {no_books} books.')
    print(f'There are {no_libraries} libraries.')
    print(f'We have {no_days} days available.')
    return books, libraries, {'no_days': no_days, 'no_libraries': no_libraries, 'no_books': no_books}


# def print_lib(lib):
#     for line in lib:
#         for i in line:
#             print(i, end=' ')
#         print('')

if __name__ == '__main__':
    main()
