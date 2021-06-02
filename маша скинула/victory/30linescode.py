import sys
sys.path.append(r'c:\python38\lib\site-packages')
import keyboard
import random
import time
import os
from shutil import get_terminal_size

s =""
text = open('baza.txt', 'r').read()
with open('baza.txt') as f:
    line_count = 0
    for line in f:
        line_count += 1
random1 = random.randint(1, line_count)
textf = open('baza.txt').readlines()
length_textf = len(textf)
a = textf[random1 - 1]
len_a = len(a)
print(a)
time1 = time.time()
for i in a:
    #print("\n" * get_terminal_size().lines, end='')
    key = keyboard.read_key()
    if key == "space":
        s = " "
    else:
        s = key
    print(s, end = "")
time2 = time.time()
print(time2 - time1)
print(len_a/(time2 - time1))






'''
    layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                           "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
print("Dctv Ghbdtn".translate(layout))
'''
    




#print(a)
#print(len_a)






'''
    layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                           "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
print("Dctv Ghbdtn".translate(layout))
'''
    




#print(a)
#print(len_a)