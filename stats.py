def get_num_words(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as file:
        book_text = file.read()
        num_words = book_text.split()
        return len(num_words)


def get_num_char(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as file:
        book_text = file.read()
        chars = list(book_text.lower())
        char_dict = {}
        for char in chars:
            if char in char_dict:
                char_dict[f"{char}"] += 1
            else:
                char_dict[f"{char}"] = 1

    return char_dict

def sort_on(dict):
    return dict["count"]

def print_report(char_dict):
    dict_list = []

    for char in char_dict:
        dict_list.append(dict(char=char, count=char_dict[f"{char}"]))

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list