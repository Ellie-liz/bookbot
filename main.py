def main():
    file_path = "books/frankenstein.txt"
    char_count = {}
    dict_list = []
    alpha_list = []
    file_contents = file_reader(file_path)
    word_count = word_counter(file_contents)
    #print(f"{word_count} words in {file_path}.")
    char_count = char_counter(file_contents)
    #char_count = char_counter("Hello World")
    dict_list = make_list(char_count)
    alpha_list = only_alpha(dict_list)
    alpha_list.sort(reverse=True, key=sort_on)
    #print(alpha_list)
    write_report(file_path, word_count, alpha_list)
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
    for d in dictionary:
        temp_dict["letter"] = d
        temp_dict["num"] = dictionary[d]
        new_list.append(temp_dict.copy()) #appending a reference overwrites so fixed with .copy() method
    return new_list
def only_alpha(list_in):
    alpha_list = []
    for l in list_in:
        if l["letter"].isalpha():
            alpha_list.append(l)
    return alpha_list
def sort_on(dictionary):
    return dictionary["num"]
def write_report(file_path, word_count, alpha_list):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    for l in alpha_list:
        letter = l["letter"]
        num = l["num"]
        print(f"The '{letter}' character was found {num} times")
    print("--- End report ---")
main()