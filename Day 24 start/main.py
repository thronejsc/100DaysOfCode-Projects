# TODO: Create a letter using starting_letter.txt


with open("../Day 24 start/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("../Day 24 start/Input/Names/invited_names.txt") as name_file:
    # return each line as a list
    names = name_file.readlines()
    for name in names:
        strip_name = name.strip("\n")
        # replace the name to each letter
        new_letter = letter.replace("[name]", strip_name)
        # create a new file for each letter ex. (letter_for_(name).txt)
        with open(f"../Day 24 start/Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as to_send:
            to_send.write(new_letter)




#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp