import random
import time
import subprocess
import os
  
# Get the size
# of the terminal

  

show = 1

while show is 1:
    size = os.get_terminal_size()
    colums = size.columns
    time.sleep(0.015)
    string = ""
    while len(string) < colums - 1:
        string = string + str(random.choice([0,1, " "]))
    print(string)