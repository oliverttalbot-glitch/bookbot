import sys

#if length of sys.argv isn't 2, print message "Usage: python3 main.py <path_to_book>" else continue
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#replace sys.arg with another variable
book_path = sys.argv[1]

# this function returns the word count and chracter count dictionary of a string given a string
from stats import get_num_words, get_chara_dict
from stats import get_book_text
from stats import sort_chara_list

#helper function that takes dictionary and returns the value of the "num" key
def sort_on(items):
    return items["num"]

#capture chara_numbers dictionary in a new variable
dictionary = get_chara_dict(get_book_text(book_path))

#call sort_chara_list with  franken_dictionary and capture it in a new variable
sorted_list = sort_chara_list(dictionary)

#function that prints sorted list and removes non alphabaic characters
def sorted_characters(items):
    #takes each little dictionary and uses the char vaule and num value to print sorted list
    for entry in items:
        if entry["char"].isalpha() == True:
            print(f"{entry['char']}: {entry['num']}")

    

# this function uses get_book_text and word_count to print a word count
def main(filepath):
    text = get_book_text(filepath)
    count = get_num_words(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    sorted_characters(sorted_list)
    print("============= END ===============")
   


main(book_path)
