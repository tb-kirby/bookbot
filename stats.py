# stats.py
# functions for word and character count in strings
# tb-kirby
# blukirby@gmail.com

def get_word_count(book_text):
    text_list = book_text.split()
    return len(text_list)

def get_char_count(book_text):
    char_dict = {}
    lower_text = book_text.lower()
    # for each character in book_text,
    #   lowercase it,
    #   if its not in the dictionary,
    #       create a key for it and set it to 1
    #   if it is in the dictionary,
    #       increment the key by 1
    for char in lower_text:
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict

def sort_char_count(char_counts):
    dict_list = []
    for key in char_counts:
        if key.isalpha():
            dict_list.append({"char": key, "num": char_counts[key]})
    dict_list.sort(key=lambda dict: dict["num"], reverse=True) 
    return dict_list
