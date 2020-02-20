from typing import List, Dict, Tuple
from main import main, LibSubmission, write_submission, Book, Library

from statistics import mean


class Search:
    def __init__(self, books: List[Book], libraries: List[Library], no_days: int) -> None:
        self.books_processed: Dict[int, Library] = {}
        self.libraries_remaining: List[Library] = []
        self.processed_libraries: List[Library] = []
        for library in libraries:
            self.libraries_remaining.append(library)
<<<<<<< HEAD
        self.days_remaining = no_days
        self.books = books
        print(books)
=======
        self.days_remaining: int = no_days
        self.books: List[Book] = books
>>>>>>> 13812f18cbae561fc50d90d3ba3c11485381259f

    def greedy_search(self) -> List[Library]:
        while (self.days_remaining > 0 and len(self.libraries_remaining) > 0):
            self.iteration(self.libraries_remaining)
        return self.processed_libraries


<<<<<<< HEAD
    def order_books(self, books):
        unique_books = self.get_unique_books(lib_books)

        sorted_score_books = sort(lambda x: x.score, unique_books)
        
        ordered_books = []
        for book in sorted_score_books:
            ordered_books.append(book)
        for book in books:
            if book not in ordered_books:
                ordered_books.append(book)
            


    def iteration(self,libraries):
=======
    def iteration(self, libraries: List[Library]) -> None:
>>>>>>> 13812f18cbae561fc50d90d3ba3c11485381259f
        local_scores = []
        max_score = -1
        best_lib = -1
        for idx, library in enumerate(libraries):
            score = self.get_local_score(library)
            if score > max_score:
                max_score = score
                best_lib = idx
            local_scores.append(score)
        self.sign_up(libraries[best_lib])
        del self.libraries_remaining[best_lib]


    def sign_up(self, library: Library) -> None:
        lib_books = []
        for book in library.books_in:
            lib_books.append(self.books[book])
        unique_books = self.get_unique_books(lib_books)
        for book in unique_books:
            self.books_processed[book.idx] = library

        self.days_remaining -= library.time_to_signup
        self.processed_libraries.append(library)


    def get_unique_books(self, books: List[Book]) -> List[Book]:
        unique_books = []
        for book in books:
            if book.idx not in self.books_processed:
                unique_books.append(book)
        return unique_books


    def get_local_score(self, library: Library) -> float:
        books = library.books_in
        lib_books = []
        for book in books:
            lib_books.append(self.books[book])
        unique_books = map(lambda x: x.score, self.get_unique_books(lib_books))
        mean_score_unique_books = mean(unique_books)
        number_of_books_per_day =-1
        number_of_books_in_library = -1
        signup_time = -1

        score =  (mean_score_unique_books * number_of_books_in_library * number_of_books_per_day) / signup_time
        return score


if __name__ == "__main__":
    books, libraries, d = main()
    print(books)
    search = Search(books, libraries, d['no_days']) 
    libraries = search.greedy_search()
    print('done')
    print(libraries)
    lib_submissions = list(map(lambda x: LibSubmission(id=x.idx, books=x.books_in), libraries))
    write_submission(lib_submissions, 'result')
