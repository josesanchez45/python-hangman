import random
import hangmanPrint
#Step 1 

word_list = ["aardvark", "baboon", "camel"]
endOfGame = False
lives = 6

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print(chosen_word)
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
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You Lose, better luck next time")

    print(f"{' '.join(display)}")

    if '_' not in display:
        endOfGame = True
        print("You win!")
    print(hangmanPrint.stages[lives])

