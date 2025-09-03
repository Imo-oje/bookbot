from stats import count_words, count_char
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as file:
        content = file.read()
    return content


def main():
    book = get_book_text(sys.argv[1])
    word_count = count_words(book)
    char_count = count_char(book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(char_count)
    print("============= END ===============")


main()
