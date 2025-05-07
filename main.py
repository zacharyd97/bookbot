from stats import get_word_count
from stats import get_chars
from stats import sort_on
from stats import sortable_dict
import sys

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    word_count = get_word_count(file_path)
    chars = get_chars(file_path)
    new_dict = sortable_dict(chars)
    new_dict.sort(reverse=True, key=sort_on)

    def get_books_text(file):
        with open(file) as f:
            file_contents = f.read()
        print(file_contents)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at{file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(len(new_dict)):
        print (f"{new_dict[i]["item"]}: {new_dict[i]["num"]}" )
    
main()  