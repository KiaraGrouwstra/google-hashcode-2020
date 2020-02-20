from typing import List, Dict, Tuple
from main import Book, Library, LibSubmission
import math

def round_down(n: int, decimals: int=0) -> int:
    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier) / multiplier)

def establish_books_per_library(D: int, library_order: List[int], books_per_day: Dict[int, int], sign_up_times: Dict[int, int]) -> List[Tuple[int, int]]:
    number_of_books_sent_by_library = []
    for library in library_order:
        if D-sign_up_times[library] < 0:
            break
        else:
            D = D-sign_up_times[library]
            number_of_books_sent_by_library.append((library, round_down(D*books_per_day[library])))  
    return number_of_books_sent_by_library

def gimme_books_printed(number_of_books_sent_by_library: List[Tuple[int, int]], book_order_in_library: Dict[int, List[int]]) -> List[int]:
    books_printed = []
    for (lib_idx, books_scanned) in number_of_books_sent_by_library:
        count = 0
        for book in book_order_in_library[lib_idx]:
            books_printed.append(book)
            count = count+1
            if count == books_scanned:
                break
    return list(set(books_printed))

def gimme_score(books_printed: List[int], book_scores: Dict[int, int]) -> int:
    score = 0 
    for book in books_printed:
        score += book_scores[book]
    return score

def evaluate(D: int, library_order: List[int], book_order_in_library: Dict[int, List[int]], books_per_day: Dict[int, int], sign_up_times: Dict[int, int], book_scores: Dict[int, int]) -> int:
    number_of_books_sent_by_library = establish_books_per_library(D, library_order, books_per_day, sign_up_times)
    books_printed = gimme_books_printed(number_of_books_sent_by_library, book_order_in_library)
    score = gimme_score(books_printed, book_scores)
    return score

def eval_lib_submissions(lib_submissions: List[LibSubmission], no_days: int, libraries: List[Library], books: List[Book]) -> int:
    return evaluate(D=no_days,
                    library_order=list(map(lambda sub: sub.id, lib_submissions)),
                    book_order_in_library = dict(map(lambda sub: (sub.id, sub.books), lib_submissions)),
                    books_per_day = dict(map(lambda lib: (lib.idx, lib.scan_per_day), libraries)),
                    sign_up_times = dict(map(lambda lib: (lib.idx, lib.time_to_signup), libraries)),
                    book_scores = dict(map(lambda book: (book.idx, book.score), books)))
