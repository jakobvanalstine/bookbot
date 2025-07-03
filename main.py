# main.py

import sys
import os.path
from stats import word_count
from stats import chr_count
from stats import sorted_list_of_chr_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        text = get_text(path)
        w_count = word_count(text)
        chr_dict = chr_count(text)
        sorted_dicts = sorted_list_of_chr_dict(chr_dict)
    except Exception as e:
        print(e)

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")

    print(f"Found {w_count} total words")

    print(f"--------- Character Count -------")

    for entry in sorted_dicts:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


def get_text(path):
    with open(path) as f:
        return f.read()

main()

