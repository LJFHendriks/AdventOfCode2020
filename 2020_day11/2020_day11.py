import numpy as np

def adjacents(arr,ival,jval):
    adjacents = ""
    for i in range(max(0, ival - 1), min(ival + 1, len(arr) - 1) + 1):
        for j in range(max(0, jval - 1), min(jval + 1, len(arr[i]) - 1) + 1):
            if i != ival or j != jval:
                adjacents += arr[i][j]
    return adjacents

def empty(adjacents):
    if "#" in adjacents:
        return "L"
    return "#"

def occupied(adjacents):
    if adjacents.count("#") >= 4:
        return "L"
    return "#"

def floor(adjacents):
    return "."

funcdic = {
    "L": empty,
    "#": occupied,
    ".": floor
}



def round(arr):
    newarr = []
    for i in range(len(arr)):
        newarr.append("")
        for j in range(len(arr[i])):
            func = funcdic[arr[i][j]]
            newarr[i] += func(adjacents(arr,i,j))
    return newarr

def day11part1():
    f = open("input.txt")
    str = f.read()
    f.close()
    arr = str.split("\n")

    newarr = round(arr)
    while newarr != arr:
        arr = newarr
        newarr = round(arr)

    sum = 0
    for i in arr:
        sum += i.count("#")

    return sum

def adjacents2(arr,i,j):
    adjacents = ""
    for di in range(-1,2):
        for dj in range(-1,2):
            if di != 0 or dj != 0:
                adjacents += scan(arr,i,j,di,dj)
    return adjacents

def scan(arr,i,j,di,dj):
    i += di
    j += dj
    while i < len(arr) \
        and j < len(arr[i]) \
        and i > -1 \
        and j > -1:
        if arr[i][j] == "#":
            return "#"
        if arr[i][j] == "L":
            return "L"
        i += di
        j += dj
    return "."

def round2(arr):
    newarr = []
    for i in range(len(arr)):
        newarr.append("")
        for j in range(len(arr[i])):
            func = funcdic2[arr[i][j]]
            newarr[i] += func(adjacents2(arr,i,j))
    return newarr

def occupied2(adjacents):
    if adjacents.count("#") >= 5:
        return "L"
    return "#"

funcdic2 = {
    "L": empty,
    "#": occupied2,
    ".": floor
}

def day11part2():
    f = open("input.txt")
    str = f.read()
    f.close()
    arr = str.split("\n")
    newarr = round(arr)
    while newarr != arr:
        arr = newarr
        newarr = round2(arr)

    sum = 0
    for i in arr:
        sum += i.count("#")

    return sum

print(f"The number of occupied seats in equilibrium in task 1 equals: {day11part1()}")
print(f"The number of occupied seats in equilibrium in task 2 equals: {day11part2()}")