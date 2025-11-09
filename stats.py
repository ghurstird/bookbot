def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts.keys():
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_list(char_counts):
    sorted_list = []
    for key in char_counts:
        temp_dict = {"char": key, "num": char_counts[key]}
        sorted_list.append(temp_dict)
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def sort_on(dict):
    return dict["num"]