import random
import hangmanPrint
import WordList
#Step 1 

WordList.word_list
endOfGame = False
lives = 6
guessedWords = []

print(hangmanPrint.logo)
#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(WordList.word_list)
#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
word_length = len(chosen_word)
display = []
for letter in chosen_word:
    display.append('_')


print(display)

while not endOfGame:
    guess = input("Hello player! Please guess a letter\n").lower()
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    for point in range(word_length):
        letter = chosen_word[point]
        if letter == guess:
            display[point] = letter
            guessedWords.append(guess)
            
    print(hangmanPrint.stages[lives])

    for word in guessedWords:
        if guess == word:
            print(f"You've already guess {guess}")

    if guess not in chosen_word and guess not in guessedWords:
        lives -= 1
        print(f"Sorry {guess} is not in the word.")
        guessedWords.append(guess)
        
        if lives == 0:
            endOfGame = True
            print("You Lose, better luck next time")


    print(f"{' '.join(display)}")

    if '_' not in display:
        endOfGame = True
        print("You win!")


