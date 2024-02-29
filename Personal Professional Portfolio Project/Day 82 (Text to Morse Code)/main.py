morse_dict = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----"  
}
    
text = input("Enter a phrase/sentece to convert: ").upper()

def text_to_morse(text):
    if len(text.split()) == 1:
        converted_text = ""
        for i in text:
            converted_text += morse_dict[i]
            converted_text += " "
        print(converted_text)

    else:
        text_list = []
        for word in text.split():
            initial_text = ""
            for letter in word:
                initial_text += morse_dict[letter] 
                initial_text += " "
            text_list.append(initial_text)
        final_code = "  ".join(text_list)
        print(f'Output:\n{final_code}')
   
text_to_morse(text)