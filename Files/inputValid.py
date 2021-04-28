import pyinputplus as pyip
import random, time

correct = 10

for i in range(10):
    print(random.randint(0, 9) + 'X' + random.randint(0, 9) +' = ')
    pyip.inputInt()