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

def sorted_list_of_chr_dict(chr_dict):
    if type(chr_dict) != dict:
        raise TypeError("Error: not a dictionary")

    def sort_on(items):
        return items["num"]

    list_of_dict = []
    for dict_key in chr_dict:
        dict_value = chr_dict[dict_key]
        list_of_dict.append({"char": f'{dict_key}', "num": dict_value})

    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

