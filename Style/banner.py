import os
import random

class colors:
    yellow =  '\033[1;33m'

def banner():
    path ='C:\Users\Administrator\Documents\GitHub\DeadTrap\Style'
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    f = open(f'C:\Users\Administrator\Documents\GitHub\DeadTrap\Style{files[index]}' , 'r')
    contents = f.read()
    print(colors.yellow + contents)
    f.close()
