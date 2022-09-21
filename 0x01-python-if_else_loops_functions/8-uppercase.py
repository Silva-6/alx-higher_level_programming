#!/usr/bin/python3
def uppercase(str):
    l = [i for i in range(97, 123)]
    u = [j for j in range(65, 91)]
    new_str = ""
    for letter in str:
        for upper, lower in zip(u, l):
            if letter == chr(lower):
                letter =  chr(upper)
        new_str += letter
    print(f"{new_str}")
