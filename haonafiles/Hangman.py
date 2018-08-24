while True:
    word = input("Type a word for someone to guess:")
    #converts the word to lowercase
    word = word.lower()
    #Check if only letters are present
    if(word.isalpha() == False):
        print("That's not a word!")
    else:
        print("Word set!")
        break

done = False
guesses = []
maxfails = 7
numfails = 0

wordToGuess = []
for letter in word:
    wordToGuess.append("_")
print("Current word:", wordToGuess)

while not done:

    # allow the user to guess single letters
    letter = input("Guess a letter:")
    # check that the user guess is a single letter

    if len(letter) > 1:
        print ("That's too long! Try again.")
    elif letter.isalpha() == False:
        print ("That's not a word! Try again.")
    else:
        # we have a single letter guessed
        # check if it's correct
        if letter in word:
            #if it is correct, show it onscreen in the hidden Word
            for idx in range(0, len(wordToGuess)):
                if (word [idx] == letter):
                    wordToGuess[idx] = letter
            print("You got a correct letter!")
            print(wordToGuess)

            done = True
            for idx in range(0, len(wordToGuess)):
                if wordToGuess[idx] == "_":
                    done = False
                    break
            if done:
                print("You won!")
                break
        else: #incorrect
        #if it's not correct, decrease number of remaining chances
            numfails += 1
            print("Chances left:", str(maxfails - numfails))

            # and let the user know they got it wrong
            print("Wrong guess!")
            if numfails >= maxfails:
                print("You Lose!")
                break


        # either way. let user know/track what letters they've guessed so far
    guesses.append(letter)
    print("guesses so far:", guesses)

#if letter.isalpha():
    #blah
#else:
    #if len(letter) > 1:
        #blah blah
    #else: # blah blah blah
#if letter.isalpha(:




    #incorrect letterhandling - error message

# ask for user to input a letter
# check to see if the letter is in the Word
# if the letter is in the word, display it and show a message that the user got it straight#if the letter os in the word, notify the user that they have one chance left
# if the letter is not in the word, notify the user that they have one chance left
# either way check the letter(s) that havebeen guessed

# display blank letters for secret Word
# display letters that the user has guessed correctly
#track wrong guesses until the user has gu
