import random
import time
import os

while True:
    size = os.get_terminal_size()
    colums = size.columns
    time.sleep(0.015)
    string = ""
    while len(string) < colums - 1:
        string = string + str(random.choice([0,1, " "]))
    print(string)