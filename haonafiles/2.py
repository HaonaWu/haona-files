i = 7
while True:
    i += 1

    if(i > 20):
        break

    # i is odd
    if(i % 2 != 0):
        continue

    print(i)

# start of -1
# add 1 to -1 which equals 0
# is 0 greater than 20? no so we do not break
# is 0 % 2 equal to 0? yes it is so we do not continure
# we go straight to our print statement
# so we print 0 first
