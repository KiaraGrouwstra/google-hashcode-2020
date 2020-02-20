import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
                
def establish_books_per_library(D, library_order, books_per_day, sign_up_times):
    number_of_books_sent_by_library = []
    for library in library_order:
        if D-sign_up_times[library] < 0:
            break
        else:
            D = D-sign_up_times[library]
            number_of_books_sent_by_library.append((library, round_down(D*books_per_day[library])))  
    return number_of_books_sent_by_library

def gimme_books_printed(number_of_books_sent_by_library, book_order_in_library):
    books_printed = []
    for library in number_of_books_sent_by_library:
        count = 0
        for book in book_order_in_library[library[0]]:
            books_printed.append(book)
            count = count+1
            if count == library[1]:
                break
    return list(set(books_printed))

def gimme_score(books_printed, book_scores):
    score = 0 
    for book in books_printed:
        score += book_scores[book]
    return score

def evaluate(days, library_order, book_order_in_library, books_per_day, sign_up_times, book_scores):
    number_of_books_sent_by_library = establish_books_per_library(days, library_order, books_per_day, sign_up_times)
    books_printed = gimme_books_printed(number_of_books_sent_by_library, book_order_in_library)
    score = gimme_score(books_printed, book_scores)
    return score
  
'''

EXAMPLE DATA 


book_order_in_library = dict()
book_order_in_library[0] = [0,1,2,3,4]
book_order_in_library[1] = [5,2,3]

library_order = [1,0]

sign_up_times = dict()
sign_up_times[0] = 2
sign_up_times[1] = 1

D = 6

books_per_day = dict()
books_per_day[0] = 1
books_per_day[1] = 2

book_scores = dict()
book_scores[0] = 1
book_scores[1] = 2
book_scores[2] = 1
book_scores[3] = 2
book_scores[4] = 1
book_scores[5] = 1  
   
''' 