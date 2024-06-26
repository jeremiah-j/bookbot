def main():
    book_path = "books/frankenstein.txt"
    book_only = book_path[6:-4]
    book = get_book(book_path)
    words = word_count(book)
    # print(f"{book_path[6:-4]}: {words} words")
    print(f"--- Begin book report of {book_only} ---")
    print(f"{words} words found in document")
    print()
    character_dict = get_characters(book)
    sorted_dict = sort_dict(character_dict) 
    print_report(sorted_dict)    
    # print(f"Sorted? {sorted_dict}")


def get_book(path):
    with open(path) as f:
        return f.read()

def word_count(book_string):
    return len(book_string.split())  

def get_characters(book, all_chars=False):
    book = book.lower()
    char_dict = {}
    for letter in book:
        if not all_chars:
            if letter in 'qwertyuioplkjhgfdsazxcvbnm':
                if letter not in char_dict:
                    char_dict[letter] = 0
                else:
                    char_dict[letter] += 1
        else:
            if letter not in char_dict:
                char_dict[letter] = 0
            else:
                char_dict[letter] += 1

    return char_dict

def sort_dict(d):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dict_list = []
    for letter in alphabet:
        for i in d:
            if letter == i:
                dict_list.append((i,d[i]))
    return dict_list 

def print_report(sorted_dict_list):
    # print(f"PRINT REPORT : {sorted_dict_list}")
    for letter in sorted_dict_list:
        print(f"The '{letter[0]}' character was found {letter[1]} times")

    

main()
