"""This snippet of a code is for backward iteration wrapping through a list. 
It starts at the 15th item in the list and goes down to 1 then continues
from the end of the list to arrive at 15th item again where it terminates"""

mylist = "abcdefghijklmnopqrstuvqxyz"
i = end = 15
while True:
    val = mylist[i]
    print(i, val)
    i -= 1
    if i % len(mylist) == end:
        break
