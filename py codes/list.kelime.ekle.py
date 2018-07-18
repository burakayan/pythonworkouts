import time

words = "ant bat cat dog"

print("the current word list contains  " + words)
time.sleep(2)

print("do you want to add a new word to the list ? ")
time.sleep(2)

again = "yes" #diving into while loop, boolean magic must be "true"

while again == "yes" :
    print("type your new word here")
    time.sleep(2)

    words = words.split()

    words.append(input())


    words = str(words) # we want to see latest version of list, change it to string value

    print("the latest list of words is" + words)

    time.sleep(2)

    print("type 'yes' to continue adding new words")
    again = input()
