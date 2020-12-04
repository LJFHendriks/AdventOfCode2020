import numpy as np

def day2part1(filename):
    f = open(filename)

    str = f.read()
    f.close()

    str = str.replace(": "," ")
    str = str.replace("-", " ")

    arr = np.array(str.split())
    arr = arr.reshape((int(arr.size/4),4))

    passwords = 0
    for i in range(arr.shape[0]):
        count = arr[i,3].count(arr[i,2])
        if int(arr[i,0]) <= count and count <= int(arr[i,1]):
            passwords += 1
    return passwords

def day2part2(filename):
    f = open(filename)

    str = f.read()
    f.close()

    str = str.replace(": ", " ")
    str = str.replace("-", " ")

    arr = np.array(str.split())
    arr = arr.reshape((int(arr.size / 4), 4))

    passwords = 0
    for i in range(arr.shape[0]):
        if (arr[i,3][int(arr[i, 0])-1] == arr[i,2]) ^ (arr[i,3][int(arr[i, 1])-1] == arr[i,2]):
            passwords += 1
    return passwords

print(f"The number of correct passwords in task 1 equals: {day2part1('input.txt')}")
print(f"The number of correct passwords in task 2 equals: {day2part2('input.txt')}")