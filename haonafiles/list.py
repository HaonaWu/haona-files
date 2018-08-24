#anExample = "Ada!"
#print(len(anExample))
# Output:4
#print("Ad" in anExample)
# Output:True
#print(anExample[2])
# Output:a
#print(anExample[2] + anExample[1])
# Output: ad
#for letter in anExample:
    #print(letter)
# Output: A
# Output: d
# Output: a
# Output: !

#checkletter = ["Girls Who Code"]
#checkletter.append("Hello")
#for letter in checkletter:
    #print(letter)

#name= ["Lovely", "Ramisa", "Haona"]

#name.insert(1, "Tova")
#print(name)

#list = ["Meem", "Toba", "Tasfia", "Anie", "Dulce"]
#for j in list:
    #print(j)

#list = ["Meem", "Toba", "Tasfia", "Anie", "Dulce"]
#list[4]="Ramisa"
#print (list)



#ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]

#total = 0

#for age in ages:
    #total += age

#average = total / len(ages)

#print(average)


# To make sure only letter is acceptable
while True:
    word = input("Type a word for someone to guess:")
    if(word.isalpha() == False):
        print("That's not a word!")
    else:
        print("Word set!")
        break

done = False

guesses = []
maxfails = 7
fails = 0
display = []

for letter in word:
    display.append("_")

while not done:
    guess = input("Guess a letter:")
    if guess in word:
        print("Correct!")
        print(letter)
    else:
        fails += 1
        print("Incorrect, you have", str(maxfails - fails))
    if letter in word:
        if done:
           print("You Win!")
    if fails == 7:
        print("Game over, too many tries")
        break
