#!/usr/bin/python3

import os

file = "37366.zip"

def unzip():
    global file
    global password
    os.system("unzip -l " + file + " | cut -d' ' -f10- | grep -Eo '[0-9]{2,5}' > " + "data")
    with open("data", "r") as f:
        for line in f:
            password = line.strip()
    os.system(f"unzip -P {password} {file}")
    file = password + ".zip"
    unzip()
    
unzip()