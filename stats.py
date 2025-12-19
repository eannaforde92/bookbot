def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_char_counts(char_counts):
    chars_list = []

    for char, count in char_counts.items():
        chars_list.append({"char": char, "num": count})

    def sort_on(dict):
        return dict["num"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

