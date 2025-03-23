import sys

from stats import get_num_words
from stats import get_num_char
from stats import print_report

def get_char_count(dict_list):

    output_str = ""
    for char_dict in dict_list:
        if char_dict["char"].isalpha():
            output_str += f"{char_dict['char']}: {char_dict['count']}\n"

    return output_str


def main():

    if sys.argv.__len__() < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    report = (f"============ BOOKBOT ============\n"
              f"Analyzing book found at {sys.argv[1]}...\n"
              f"----------- Word Count ----------\n"
              f"Found {get_num_words(sys.argv[1])} total words\n"
              f"--------- Character Count -------\n"
              f"{get_char_count(print_report(get_num_char(sys.argv[1])))}"
              f"============= END ===============")

    print(report)

main()