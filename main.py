# main.py

from stats import word_count
from stats import chr_count

def main():
    path = "./books/frankenstein.txt"

    try:
        text = get_text(path)
        w_count = word_count(text)
        chr_dict = chr_count(text)
    except Exception as e:
        print(e)
        raise

    print(f"{w_count} words found in the document")
    print(chr_dict)


def get_text(path):
    if type(path) != str:
        raise TypeError("Error: not a string")

    with open(path) as f:
        return f.read()

main()

