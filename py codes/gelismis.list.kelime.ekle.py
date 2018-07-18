def checkword():
    
    if input() in words:
        time.sleep(2)
        print("the word has been previously added to the list")
    else:
        time.sleep(2)
        print("the word doesn't exist in current list")
    time.sleep(2)
    # print("type 'yes' if you want to add the word") "i want to turn back to first while loop
    # again = input().lower()
    
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

    words.append(input().lower())


    words = str(words) # we want to see latest version of list, change it to string value

    print("the latest list of words is" + words)

    time.sleep(2)

    print("type 'yes' to continue adding new words")
    again = input().lower()
    time.sleep(1)


time.sleep(2)
print("type 'yes' for checking the words in the list")   
search = input()

while search == "yes" :
    words.split()
    
    print("please type the word you want to search in the list")
    time.sleep(1)
    
    checkword()
    

