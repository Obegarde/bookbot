frankenstein_path = "books/frankenstein.txt"



def load_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def give_word_count(book_string):
    word_array = book_string.split()
    word_count = len(word_array)
    return word_count

def give_character_count(book_string):
    char_dict = {}
    for char in book_string.lower():
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict(char_dict):
    return dict(sorted(char_dict.items(), key = lambda item: item[1], reverse=True))

def report_maker(book_path):
    book_string = load_book(book_path)
    char_dict = give_character_count(book_string)
    sorted_dict = sort_dict(char_dict)
    word_count = give_word_count(book_string)
    report_string = f"---Begin report of {book_path}---\n{word_count} words found in the document\n\n"
    for key in sorted_dict:
        if key == "\n":
            report_string = report_string + f"The '\\n' character was found {sorted_dict[key]} times\n"
        else:
            report_string = report_string + f"The '{key}' character was found {sorted_dict[key]} times\n"

    report_string = report_string + "--- End Report ---"
    return report_string


