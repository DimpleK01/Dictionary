import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    
    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys()))>0:
        for i in range(len(get_close_matches(word, data.keys()))):
            print("Did you mean %s instead?" %get_close_matches(word, data.keys())[i])
            option=input("select y or n\n")
            if option.lower()=='y':
                return data[get_close_matches(word, data.keys())[i]]
            elif option.lower()=='n':
                continue
            else:
                print("Sorry, no such option exists")
        else:
             print("Sorry, this word does not exist")

    else:
        print("Sorry, this word does not exist")

word = input("Enter the word to be searched\n")

definition = meaning(word)
if type(definition)==list:
    for item in definition:
        print(item)

