import numpy as np

def isSum(arr,val):
    for i, val1 in enumerate(arr):
        for j, val2 in enumerate(arr):
            if val1+val2 == val and i != j:
                return True
    return False

def day9part1():
    f = open("input.txt")
    str = f.read()
    f.close()
    arr = str.split("\n")
    arr = np.array(arr, dtype=np.int64)

    pre = 25
    loc = pre
    while isSum(arr[loc-pre:loc],arr[loc]):
        loc += 1
    return arr[loc]


def day9part2():
    f = open("input.txt")

    str = f.read()
    f.close()
    arr = str.split("\n")
    arr = np.array(arr, dtype=np.int64)

    val = day9part1()

    for i in range(len(arr)):
        sum = 0
        pos = 0
        while sum <= val:
            sum += arr[i+pos]
            pos += 1
            if sum == val:
                return min(arr[i:i+pos]) + max(arr[i:i+pos])
    return 0


print(f"The first number that does not follow the pattern equals: {day9part1()}")
print(f"The encryption weakness equals: {day9part2()}")