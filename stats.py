# this function returns the contents of a text file from a filepath
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

# this function returns the word count of a string given a string
def get_num_words(text):
    #split the string into individual words
    word_list = text.split()
    #count the list
    word_count = len(word_list)
    return word_count

#this function returns the number of each character that appears in a string
def  get_chara_dict(text):
    #convert all characters to lowercase
    characters = text.lower()
    #use a loop to create a dictionary containing the integer values of each character
    chara_dict = {}
    for chara in characters:
        if chara not in chara_dict:
            chara_dict[chara] = 1
        else: chara_dict[chara] += 1
    return chara_dict

#helper function that takes dictionary and returns the value of the "num" key
def sort_on(items):
    return items["num"]

#function that takes the dictionary of characters and returns a sorted list of dictionaries
def sort_chara_list(chara_dict):
    #empty list
    result = []
    #loop over the dict and append the values to the list in their own little dictionaries
    #dict.items() creates tuples
    for chara, count in chara_dict.items():
        #appends the tuple pairs in the list to their own little dictionaries
        result.append({"char": chara, "num": count})
    result.sort(reverse=True, key=sort_on)
    return result