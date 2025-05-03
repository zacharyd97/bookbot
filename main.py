from stats import get_word_count
from stats import get_chars
from stats import sort_dict


def main():
    file_path = "books/frankenstein.txt"
    word_count = get_word_count(file_path)
    chars = get_chars(file_path)


    def get_books_text(file):
        with open(file) as f:
            file_contents = f.read()
        print(file_contents)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at{file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(sort_dict(chars))
    
main()  