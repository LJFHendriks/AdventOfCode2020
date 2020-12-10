import numpy as np

def diff(arr):
    arr.sort()
    dif =[arr[0]]
    dif.extend(arr[1:]-arr[:-1])
    dif.append(3)

    counts = {
    }
    for i in dif:
        counts[i] = counts.get(i,0) + 1
    return counts

def day10part1():
    f = open("input.txt")
    str = f.read()
    f.close()
    arr = str.split("\n")
    arr = np.array(arr, dtype=np.int64)

    counts = diff(arr)
    return counts[1] * counts[3]

def isValid(arr):
    arr.sort()
    dif = [arr[0]]
    dif.extend(arr[1:] - arr[:-1])
    return max(dif) <= 3

def changeArr(arr,loc):
    sum = 1
    for i in range(loc,len(arr)-1):
        rem = arr[i]
        arr = np.delete(arr,i)
        if isValid(arr):
            loc = i

            sum += changeArr(arr,loc)
        arr = np.append(arr,rem)
        arr.sort()
    return sum

def testing():
    f = open("input.txt")
    str = f.read()
    f.close()
    arr = str.split("\n")
    arr = np.array(arr, dtype=np.int64)
    arr.sort()

    print(changeArr(arr, 0))

def countdiff(arr):
    arr.sort()
    dif = [arr[0]]
    dif.extend(arr[1:] - arr[:-1])
    dif.append(3)

    counts = {
    }
    count = 0
    for i in dif:
        if i == 1:
            count += 1
        elif i == 3:
            if count > 1:
                counts[count] = counts.get(count, 0) + 1
            count = 0
        else:
            "PANIC"
    return counts

def posibilityArray(maxcount):
    posArr = [1, 1, 2]
    for i in range(maxcount-2):
        posArr.append(posArr[-3] + posArr[-2] + posArr[-1])
    return posArr


def day10part2():
    f = open("input.txt")
    str = f.read()
    f.close()
    arr = str.split("\n")
    arr = np.array(arr, dtype=np.int64)

    counts = countdiff(arr)
    posArr = posibilityArray(max(counts.keys()))
    total = 1
    for key, value in counts.items():
        total *= posArr[key]**value
    return total





print(f"The number of 1-jolt differences multiplied by the number of 3-jolt differences equals: {day10part1()}")
print(f"The number of distinct ways to order the adapters equals: {day10part2()}")