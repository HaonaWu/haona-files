import random

def say_hello():
    # ask the user for their name and says hello
    name = input("Hello, my name is emily. What is your name?\n\n")
    print("Hi "  + name + " let's play rock paper scissor")

def play_game(human_score, computer_score):
    # runs the rock paper scissor game
    options = ["rock" , "paper", "scissor"]
    comp_player = random.choice(options)#computer picks random word form list
    player_answer = input ("Which would you like to play? Choose rock paper or scissor: ")
    player_answer = player_answer.lower()
    if player_answer == "rock" and comp_player == "rock":
        print("Looks like you tied! You played rock and the computer played rock.")
        try_again(human_score, computer_score)
    elif player_answer == "paper" and comp_player == "rock":
        human_score += 1
        print("Human Score: "  + str(human_score))
        print("Computer Score: " + str(computer_score))
        print("Looks like you win! You played paper and the computer played rock. Paper covers rock.")
        try_again(human_score, computer_score)
    elif player_answer == "scissor" and comp_player == "rock":
        computer_score += 1
        print("Computer Score: " + str(computer_score))
        print("Human Score: "  + str(human_score))
        print("Looks like you lost! You played scissor and the computer played rock. Rock beats scissor.")
        try_again(human_score, computer_score)
    elif player_answer == "paper" and comp_player == "paper":
        print("Looks like you tied! You played paper and the computer played paper.")
        try_again(human_score, computer_score)
    elif player_answer == "rock" and comp_player == "paper":
        computer_score += 1
        print("Computer Score: " + str(computer_score))
        print("Human Score: "  + str(human_score))
        print("Looks like you lost! You played rock and the computer played paper. Paper covers rock.")
        try_again(human_score, computer_score)
    elif player_answer == "scissor" and comp_player == "paper":
        human_score += 1
        print("Computer Score: " + str(computer_score))
        print("Human Score: "  + str(human_score))
        print("Looks like you win! You played scissor and the computer played paper. scissor cuts paper.")
        try_again(human_score, computer_score)
    elif player_answer == "scissor" and comp_player == "scissor":
        print("Looks like you tied! You played scissor  and the computer played scissor.")
        try_again(human_score, computer_score)
    elif player_answer == "paper" and comp_player == "scissor":
        computer_score += 1
        print("Computer Score: " + str(computer_score))
        print("Human Score: "  + str(human_score))
        print("Looks like you lost! You played paper and the computer played scissor. ")
        try_again(human_score, computer_score)
    elif player_answer == "rock" and comp_player == "scissor":
        human_score += 1
        print("Computer Score: " + str(computer_score))
        print("Human Score: "  + str(human_score))
        print("Looks like you win! Rocks beats scissor.")
        try_again(human_score, computer_score)
    else:
        print("Not a vaild input for this game!")
        play_game(human_score, computer_score)

def try_again(human_score, computer_score):
    play_again = input ("Would you like to play again, yes or no.")
    play_again = play_again.lower()
    if play_again == "yes":
        play_game(human_score, computer_score)
    elif play_again == "no":
        print("Loser! Giving up already? ok, bye.")
    else:
        print("Hmm don't think I understand.")
        try_again(human_score, computer_score)

def main():
        # run the say_hello function
        # run the play_game function
    say_hello()
    play_game(0,0)

main()
