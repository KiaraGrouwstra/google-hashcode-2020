books_processed = {}
libraries_remaining = []


local_scores = []
max_score = -1
best_lib = -1
for idx, library in enumerate(libraries):
    score = get_local_score(library)
    if score > max_score:
        max_score = score
        best_lib = idx
local_scores.append(score)
sign_up(best_lib)


def sign_up(library, unique_books):
    for book in unique_books:
        books_processed[book] = library

    del libraries_remaining[library]


def get_unique_books(library):
    books = library.get_books()
    unique_books = []
    for book in books:
        if book not in books_processed:
            unique_books.append(book)
    return unique_books


def get_local_score(library):
    unique_books = get_unique_books(library)
    mean_score_unique_books = mean(unique_books)
    number_of_books_per_day =-1
    number_of_books_in_library = -1
    signup_time = -1

    score =  (mean_score_unique_books * number_of_books_in_library * number_of_books_per_day) / signup_time
