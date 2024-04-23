"""
Word Guessing Game:

Create a Python program for a word guessing game with these rules:
1. Pick a random word from a predefined list.
2. Allow the player limited attempts to guess the word.
3. Give feedback on each guess: reveal correct letters, inform incorrect ones.
4. End the game when the word is guessed correctly or attempts run out.
5. Ask if the player wants to play again after each game.
"""

import random
words = ["python", "jumble", "wizard", "bumpy", "gaze", "fly", "quiz", "jazz", "jack", "glyph"]
name= input("What is your name?")
while True:
    final=""
    guesses=[]
    word1=[]
    wrong=0
    word=words[random.randint(0,len(words)-1)]
    for j in word:
        word1.append(j)
    guesses = ["_" for _ in word1]
    print(word1)
    print(guesses)
    while True:
        guess=input("Enter your first guess :")
        if guess in word1:
            guesses[word1.index(guess)]=word1[word1.index(guess)]
            for k in guesses:
                final=final+k
            print(final)
            if final==word:
                print("wow! congratulations! you have correctly guessed the word")
                break
            final=""
        else:
            wrong+=1
            if wrong==5:
                print("You lost")
                break
            print(f"You have made {wrong} wrong guess, you only have {5-wrong} lives now")
    again=input("Do you want to play again? (yes/no)").lower()
    if again=="yes":
        continue
    else:
        break