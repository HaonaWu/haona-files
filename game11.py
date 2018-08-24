import random

comp_player = "banana"

def say_hello():
    # ask the user for their name and says hello
    name = input("Hello, my name is emily. What is your name?\n\n")
    print("Hi "  + name + " let's play rock paper scissor")

def comp_answer_rock():
    player_answer = input ("Which would you like to play? Choose rock paper or scissor: ")
    player_answer = player_answer.lower()
    if player_answer == "rock":
        print("Looks like you tied! You played rock and the computer played rock.")
        try_again()
    elif player_answer == "paper":
        print("Looks like you win! You played paper and the computer played rock. Paper covers rock.")
        try_again()
    elif player_answer == "scissor":
        print("Looks like you lose! You played scissor and the computer played rock. Rock beats scissor.")
        try_again()
    else:
        print("Not a vaild input.")
        comp_answer_rock()

def comp_answer_paper():
    player_answer = input ("Which would you like to play? Choose rock paper or scissor: ")
    player_answer = player_answer.lower()
    if player_answer == "paper":
        print("Looks like you tied! You played paper and the computer played paper.")
        try_again()
    elif player_answer == "rock":
        print("Looks like you lost! You played rock and the computer played paper. Paper covers rock.")
        try_again()
    elif player_answer == "scissor":
        print("Looks like you win! You played scissor and the computer played paper. scissor cuts paper.")
        try_again()
    else:
        print("Not a vaild input.")
        comp_answer_paper()

def comp_answer_scissor():
    player_answer = input ("Which would you like to play? Choose rock paper or scissor: ")
    player_answer = player_answer.lower()
    if player_answer == "scissor" and comp_player == "scissor":
        print("Looks like you tied! You played scissor  and the computer played scissor.")
        try_again()
    elif player_answer == "paper" and comp_player == "scissor":
        print("Looks like you lost! You played paper and the computer played scissor. ")
        try_again()
    elif player_answer == "rock" and comp_player == "scissor":
        print("Looks like you win! Rocks beats scissor.")
        try_again()
    else:
        print("Not a vaild input.")
        comp_answer_scissor()


def try_again():
    play_again = input ("Would you like to play again, yes or no.")
    play_again = play_again.lower()
    if play_again == "yes":
        run_game()
    elif play_again == "no":
        print("Loser! Giving up already? ok, bye.")
    else:
        print("Hmm don't think I understand.")
        try_again()

def run_game():
    options = ["rock", "paper", "scissor"]
    comp_player = random.choice(options)
    if comp_player == "rock":
        comp_answer_rock()
    elif comp_player == "paper":
        comp_answer_paper()
    else:
        comp_answer_scissor()

def main():
    say_hello()
    run_game()

main()
