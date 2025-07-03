# stats.py

def word_count(text):
    if type(text) != str:
        raise TypeError("Error: not a string")

    return len(text.split())

def chr_count(text):
    if type(text) != str:
        raise TypeError("Error: not a string")

    text = text.lower()

    chr_set = set()
    for chr in text:
        chr_set.add(f'{chr}')

    chr_dict = {}
    for chr in chr_set:
        chr_dict[chr] = 0

    for chr in text.lower():
        chr_dict[chr] += 1

    return chr_dict

