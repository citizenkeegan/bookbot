def get_num_words(text):
    split_words = text.split()
    return len(split_words)

def get_char_count(text):
    final_char_count = {}
    for char in text.lower():
        if char in final_char_count:
            final_char_count[char] += 1
        else:
            final_char_count[char] = 1
    return final_char_count

def sort_on(items):
    return items["num"]

def dict_count(characters):
    result = []
    for ch, count in characters.items():
        result.append({"char": ch, "num": count})
    result.sort(reverse=True, key=sort_on)
    return result