
# main.py

import sys
import os.path
from stats import (
    word_count,
    char_count,
    sort_char_counts,
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 bookbot.py <path_to_book>")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print("Usage: python3 bookbot.py <path_to_book>")
        sys.exit(1)


    path = sys.argv[1]


    with open(path) as f:
        text = f.read()


    try:
        count = word_count(text)
        char_count_dict = char_count(text)
        sorted_char_counts = sort_char_counts(char_count_dict)
    except Exception as e:
        print(e)
        sys.exit(1)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print(f"--------- Character Count -------")

    for entry in sorted_char_counts:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()

