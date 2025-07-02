# stats.py

def word_count(text):
    if type(text) != str:
        raise TypeError("Error: not a string")

    return len(text.split())

