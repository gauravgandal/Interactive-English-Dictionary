import json #Importing Json Module to use json functions
from difflib import get_close_matches 
data = json.load(open("data.json")) # load is method of json module to open the json file
def find(word): 
    if word in data: 
        return data[word] #Since json is dict it returns the value of inputed word
    elif len(get_close_matches(word,data.keys()))>0:
        option= str.upper(input("Did you mean '%s'? Enter Y if yes , N if no : " % get_close_matches(word,data.keys())[0]))
        if option=='Y':
            yes_word=get_close_matches(word,data.keys())[0]
            print("SHOWING RESULTS FOR ' %s '" % yes_word)
            return data[yes_word]
        elif option=="N":
            return "Word not found"
        else :
            return "InValid Option"
    else:
        return "Word not found"
input_word=str.lower(input("Enter word to find meaning :"))

output=find(input_word)
if isinstance(output,list):
    for item in output:
        print(item)
else:
    print(output)


