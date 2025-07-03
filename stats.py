# stats.py

def word_count(text):
    return len(text.split())


def char_count(text):
    char_set = set()
    for char in text.lower():
        char_set.add(f'{char}')

    char_count_dict = {}
    for char in char_set:
        char_count_dict[char] = 0

    for char in text.lower():
        char_count_dict[char] += 1

    return char_count_dict


def sort_char_counts(char_count_dict):
    sorted_list = []
    for char in char_count_dict:
        count = char_count_dict[char]
        sorted_list.append({"char": char, "num": count})

    def sort_on(items):
        return items["num"]

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

