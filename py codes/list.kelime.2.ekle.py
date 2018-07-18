import time

print("this program lets you to add new words into words list")
time.sleep(2)

words = "ant bat cat dog"

print("the current list is " + words + "enter a new word to add into list")
time.sleep(2)

words = words.split()

words.append(input())

words = str(words)

print("the new word list is " + words)
