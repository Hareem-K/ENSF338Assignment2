'''
Filename: ex1.5.py
Course: ENSF 338
Group Number: 12

'''
import json
import random

with open("ex2.json", "r") as file:
    array = json.load(file)

random.shuffle(array)
for i in array:
    random.shuffle(i)

random_json = open("ex2.5.json", "w")
json.dump(array, random_json, indent = 2)