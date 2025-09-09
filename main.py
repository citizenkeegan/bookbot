import sys

from stats import get_num_words
from stats import get_char_count
from stats import sort_on
from stats import dict_count


def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text


def main():
    text = get_book_text(book_path)
    count = get_num_words(text)
    characters = get_char_count(text)
    sorted_chars = dict_count(characters)
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    book_path = sys.argv[1]
    main()
else:  
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)