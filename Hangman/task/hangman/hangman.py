import random
import string
print("H A N G M A N\n")
while True:
    print('"play" to play the game, "exit" to quit:')
    user_input = input()
    if user_input not in ['play', 'exit']:
        continue
    if user_input == "exit":
        break
    computer_selected = random.choice(['python', 'java', 'kotlin', 'javascript'])
    printed_word = "-" *(len(computer_selected))
    attempts = 8
    guess_letter = set()
    while attempts > 0:
        print()
        print(printed_word)
        letter = input('Input a letter: ')
        if len(letter) > 1:
            print("You should input a single letter")
            continue
        if letter not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
            continue
        if letter in guess_letter:
            print("You've already guessed this letter")
            continue
        guess_letter.add(letter)
        if letter in computer_selected:
            if letter in printed_word:
                print("No improvements")
                attempts -= 1
            else:
                new_printed_word = ""
                for index in range(len(computer_selected)):
                    if letter == computer_selected[index]:
                        new_printed_word += letter
                    else:
                        new_printed_word += printed_word[index]
                printed_word = new_printed_word
                if printed_word == computer_selected:
                    break
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

    if printed_word == computer_selected:
        print("You guessed the word {}!".format(printed_word))
        print("You survived!")
    else:
        print("You lost!")
