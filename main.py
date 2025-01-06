def main():
    file_path = "books/frankenstein.txt"
    char_count = {}
    dict_list = []
    file_contents = file_reader(file_path)
    word_count = word_counter(file_contents)
    print(f"{word_count} words in {file_path}.")
    char_count = char_counter(file_contents)
    #char_count = char_counter("Hello World")
    dict_list = make_list(char_count)
    print(dict_list)
#opens a text file and converts it into a string
def file_reader(path):
    with open(path) as f:
        file_text = f.read()
    return file_text
#splits string into list of words returns amount of words
def word_counter(string):
    words = string.split()
    word_count = len(words)
    return word_count
#takes string and splits into letters returns dictionary with amount per letter
def char_counter(string):
    lower_string = string.lower()
    char_count = {}
    for c in lower_string:
        char_count[c] = 0
    for d in lower_string:
        char_count[d] += 1
    return char_count
#makes a list of dictionaries
def make_list(dictionary):
    new_list = []
    temp_dict = {}
    print(dictionary)
    for d in dictionary:
        temp_dict["letter"] = d
        temp_dict["num"] = dictionary[d]
        new_list.append(temp_dict.copy()) #appending a reference overwrites so fixed with .copy() method
    return new_list 
main()