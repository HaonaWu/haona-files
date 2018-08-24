from random import randint

#Generates a random integer
RandomNumber = randint(1, 20)
# For testinf: print (RandomNumber)

numTries = 0
while True:
    Guess = input("guess a numver between 1 and 20 inclusive): ")
    numTrues += 1
    if not guess.isnumeric:
        print("that's not a positive whole number, try again")
        continue

    else(guess = int(guess))
#check number is correct
    if guess == aRandomNumber
        print("Yay you guessed the number!")
        break

#check if out of tries
    if numTries >= 3:
        print("Sorry, You guessed too many times, The number was:" + str(aRandomNumber))
        break

    #give hints
    if(guess > aRandomNumber):
        print("Try a smaller number text time!")
    else(guess< aRandomNumber):
        print("Trt a bigger number next time!")
