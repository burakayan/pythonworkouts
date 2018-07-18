import random

print(" i will flip a coin 1000 times, and try to guess how many times it will come up heads")
input()

flips = 0

heads = 0

while flips < 1000 :
    if random.randint(0,1) == 1:
        heads = heads +1
    flips = flips + 1

    if flips == 900:

        print("900 flips and there  have been " + str(heads) +" heads.")

    if flips == 100:
        print(" at 100 tosses, heads has come upp " + str(heads) + "times so far")

    if flips == 500:
        print("half way done, and heads come up " + str(heads) + "times")



print()
print("out of 1000 coin tosses, heads came up " + str(heads) + " times")

print("were you close?")



