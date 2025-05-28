# bookbot
# tb-kirby
# blukirby@gmail.com

import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count

def get_book_text(path):
    book_text = ""
    with open(path) as book:
        book_text = book.read()
    return book_text


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_counts = get_char_count(book_text)
    sorted_char_list = sort_char_count(char_counts)    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------") 
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for line in sorted_char_list:
        print(f'{line["char"]}: {line["num"]}')

main() 
