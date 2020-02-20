from evaluate import establish_books_per_library, evaluate

book_order_in_library = dict()
book_order_in_library[0] = [0,1,2,3,4]
book_order_in_library[1] = [5,2,3]

library_order = [1,0]

sign_up_times = {
    0: 2,
    1: 1,
}

D = 6

books_per_day = {
    0: 1,
    1: 2,
}

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
