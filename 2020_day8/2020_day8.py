import re

def nop(loc, acc, val):
    return loc+1,acc

def acc(loc, acc, val):
    return loc+1,acc+val

def jmp(loc, acc, val):
    return loc+val,acc

movesdic = {
    "nop": nop,
    "acc": acc,
    "jmp": jmp
}

def day8part1():

    f = open("input.txt")

    str = f.read()
    f.close()
    arr = str.split("\n")
    return isloop(arr)[2]

def isloop(arr):
    loc = 0
    acc = 0
    lochistory = []
    while loc not in lochistory:
        lochistory.append(loc)
        ope = re.search(r"^(\w+)\s([+-]\d+)", arr[loc]).groups()
        loc, acc = movesdic[ope[0]](loc, acc, int(ope[1]))
        if loc == len(arr):
            return False, lochistory, acc
    return True, lochistory, acc

def day8part2():
    f = open("input.txt")

    str = f.read()
    f.close()
    arr = str.split("\n")
    a, lochistory, c = isloop(arr)
    for i in lochistory:
        if arr[i][0:3] == "nop":
            arr[i] = re.sub(r"^\w+","jmp",arr[i])
            a, b, acc = isloop(arr)
            if not a:
                return acc
            arr[i] = re.sub(r"^\w+","nop",arr[i])
        if arr[i][0:3] == "jmp":
            arr[i] = re.sub(r"^\w+","nop",arr[i])
            a, b, acc = isloop(arr)
            if not a:
                return acc
            arr[i] = re.sub(r"^\w+","jmp",arr[i])
    return 0


print(f"The number of bags that can contain a shiny gold bag equals: {day8part1()}")
print(f"The number of individual bags inside a shiny gold bag equals: {day8part2()}")
