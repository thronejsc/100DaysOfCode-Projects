student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as p
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

letter_code = p.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter: row.code for (index, row) in letter_code.iterrows()}

def generate_phoentic():
    word = input("Enter a name: ").upper()
    try:
        code_word = [letter_dict[key] for key in word]
    except KeyError:
        print(f"Sorry, only letters are accepted")
        generate_phoentic()
    else:
        print(code_word)

generate_phoentic()
