from stats import number_of_words
from stats import count_each_character
from stats import report_part1
from stats import report_part2
import sys

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        return file_content

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    word_count = number_of_words(text)
    print(report_part1())
    print(word_count)
    print(report_part2(count_each_character(text)))

main()