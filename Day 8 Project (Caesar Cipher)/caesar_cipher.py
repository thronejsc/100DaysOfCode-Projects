alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo

print(logo)

def encrypt(text, shift):
  cypher_text = ""
  for i in text:
    if i == ' ':
      cypher_text += ' '
    else:
      shift_text = alphabet.index(i) + shift
      if shift_text > len(alphabet)-1:
        # if w , (22+9) - 25
        cypher_text += alphabet[shift_text - (len(alphabet)-1)]
      else:
        cypher_text += alphabet[shift_text]  
  print(f"Heres the encoded result: {cypher_text}")


def decrypt(text, shift):
  cypher_text = ""
  for i in text:
    if i == ' ':
      cypher_text += ' '
    else:
      shift_text = alphabet.index(i) - shift
      if shift_text < 0:
        # if w , (22+9) - 25
        cypher_text += alphabet[shift_text + (len(alphabet)-1)]
      else:
        cypher_text += alphabet[shift_text]  
  print(f"Heres the decoded result: {cypher_text}")
  
def try_again():
  a = input("Do you want to try again? (y/n) ").lower()
  if a == 'y':
    caesar_cipher()
  elif a == 'n':
    print("Thank you...")


def caesar_cipher():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if direction == "encode" or  direction == 'e':
    encrypt(text, shift)
    try_again()
  elif direction == "decode" or  direction == 'd':
    decrypt(text, shift)
    try_again()
  else:
    print("Please input a valid letter")
    try_again()
    

caesar_cipher()


    
  

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
