import numpy as np

def day3part1(right,down):
    f = open("input.txt")

    str = f.read()


    arr = str.split()

    width = len(arr[0])

    trees = 0
    pos = 0
    for i in range(0,len(arr),down):
        if arr[i][pos % width] == "#":
            trees += 1
        pos += right
    return trees

def day3part2():

    return day3part1(1,1) * day3part1(3,1) * day3part1(5,1) * day3part1(7,1) * day3part1(1,2)

print(f"The number of trees hit in task 1 equals: {day3part1(3,1)}")
