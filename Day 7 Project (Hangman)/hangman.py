# STEP 1 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# STEP 2

#TODO-6: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-7: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-8: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# STEP 3

#TODO-9: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

import random
import hangman_art , hangman_words

display = []
guessed_letters = []

random_number = random.randint(0,len(hangman_words.word_list) - 1) 
chosen_word = hangman_words.word_list[random_number]
# print(chosen_word)

for i in range (len(chosen_word)):
  display += "_"
  
print(f"\n{' '.join(display)}")

finished = False
lives = 6
print(hangman_art.stages[lives])
while finished != True:
  
  guess_letter = input("\nGuess a letter: ")
  guess_letter.lower()
  
  
  if guess_letter not in guessed_letters:
    
    for i in range (len(chosen_word)):
      if guess_letter == chosen_word[i]:
        display[i] = guess_letter
    
  
    if guess_letter not in chosen_word:
      print("Sorry it is not in the word")
      lives -= 1
      print(hangman_art.stages[lives])
    
  else:
    print(f"You've already guessed {guess_letter}") 
    
  print(f"\n{' '.join(display)}\n")
  
  guessed_letters += guess_letter
  final = ''.join(display)  
  
  if lives == 0:
    finished = True
    print("\nSorry you lose\n")
  elif chosen_word == final:
    finished = True
    print("\nCongrats you won!\n")
       

print(f"The word is: {chosen_word}\n")



