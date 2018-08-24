# --- Define your functions below! ---


# --- Put your main program below! ---
def intro():
    print("Hi, my name is ella. What is your name?\n\n")

def question1():
    print("What is your faorite season?\n\n")

def question2():
    print("What is your favorite color\n\n")

def say_greeting():
    print("Hey there!\n\n")

def say_goodbye():
    print("Bye bye")

def say_poem():
    print("Fire and Ice by Robert Frost\n\n")

def say_season():
    print("That is my favorite season too!\n\n")
    print("I'm glad that we have something in common\n\n")

def say_color():
    print("My favorite color is green\n\n")



def process_name(yourname):
    print(yourname)
    print("Nice to meet you", str(yourname))


def process_input(answer):
    output = ""
    if answer == "hi":
        say_greeting()
    elif answer == "hello":
        say_greeting()
    elif answer == "hey":
        say_greeting()
    elif answer == "bye":
        say_goodbye()
    elif answer == "poem":
        say_poem()
    elif answer == "spring":
        say_season()
    elif answer == "summer":
        say_season()
    elif answer == "fall":
        say_season()
    elif answer == "winter":
        say_season()
    elif answer == "red":
        say_color()
    elif answer == "blue":
        say_color()
    elif answer == "green":
        say_color()
    elif answer == "yellow":
        say_color()
    elif answer == "pink":
        say_color()
    elif answer == "grey":
        say_color()
    elif answer == "black":
        say_color()
    elif answer == "white":
        say_color()
    else:
        output = "that sounds fun!"
        print(output)

def chat1():
    print("")

    #farewells = ["bye","see you later","see ya"]

def main():
  intro()
  while True:
    answer = input("(Type your name:)")
    process_name(answer)


    answer = input("(What will you say?) ")
    process_input(answer)

    question1()
    answer = input("(This is a new question!)")
    process_input(answer)

    question2()
    answer = input("(This is a new question!)")
    process_input(answer)
    break

            # Display a farewell message to the user.
#def say_goodbye():
    #print("See you next time!")



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
