#!/usr/bin/python3
for num in range(100):
    if num == 99:
        print(f"{num:02}")
    else:
        print(f"{num:02}", end=", ")
