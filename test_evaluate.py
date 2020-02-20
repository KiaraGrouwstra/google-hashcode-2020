from evaluate import establish_books_per_library, evaluate

# the order in which we want to scan books for each library
book_order_in_library = {
    0: [0,1,2,3,4],
    1: [5,2,3],
}

# order in which we want to sign up the libraries
library_order = [1,0]

# dict from id of the library to how many days it takes to sign up
sign_up_times = {
    0: 2,
    1: 1,
}

# number of available days
D = 6

# dict from library id to how many books it scan per day
books_per_day = {
    0: 1,
    1: 2,
}

# dict from book id to book score
book_scores = {
    0: 1,
    1: 2,
    2: 1,
    3: 2,
    4: 1,
    5: 1,
}

def test_establish_books_per_library():
    tuples = establish_books_per_library(D, library_order, books_per_day, sign_up_times)
    assert tuples == [(1, 10), (0, 3)]

def test_evaluate():
    score = evaluate(D, library_order, book_order_in_library, books_per_day, sign_up_times, book_scores)
    assert score == 7

if __name__ == '__main__':
    test_establish_books_per_library()
    test_evaluate()
