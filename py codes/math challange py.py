#this program is a math contest. challange computer if you believe your math skills
# you are supposed to sum 2 integers. don't make mistake.

import random
import time

print("do you trust your math skills ? if so, i challange you!")

challange = ""

while challange != "x" :
    value1 = random.randint(0,1000)

    value2 = random.randint(0,1000)

    result = value1 + value2
    
    value1 = str(value1)
    value2 = str(value2)
    
    
    print("what is the sum of " + value1  + " and " + value2  + " ?")
    
    answer = input()
    answer = int(answer)
    
    if answer == result:
        time.sleep(2)
        print("it is true. you are good at math")

    else:
        time.sleep(2)
        print("your answer is false. keep up working!")
    time.sleep(2)
    print("press x to exit")
    challange = input()
    

time.sleep(2)
print("you are brave. come back soon")
time.sleep(20)
