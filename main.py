# main.py

from stats import word_count

def main():
    path = "./books/frankenstein.txt"

    try:
        text = get_text(path)
        count = word_count(text)
    except Exception as e:
        print(e)
        raise

    print(f"{count} words found in the document")


def get_text(path):
    if type(path) != str:
        raise TypeError("Error: not a string")

    with open(path) as f:
        return f.read()

main()

