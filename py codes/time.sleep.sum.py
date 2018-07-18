import time
print("this code is written for addition of 2 variables.")

time.sleep(2)

print("please enter 2 variables")
execution = ""
while execution != "x" :

    print("enter first variable")
    integer1 = input()
    integer1 = int(integer1)

    print("enter second variable")
    integer2 = input()
    integer2 = int(integer2)

    summation = integer1 + integer2

    summation = str(summation)

    print("the result is " + summation + ".")
    print("press x to exit")
    execution = input()
