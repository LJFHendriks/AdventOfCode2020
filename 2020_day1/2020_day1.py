import numpy as np

def day1part1(filename):
    f = open(filename)

    arr = f.read().split()
    f.close()

    arr = np.array(arr,dtype=int)
    for i in arr:
        for j in arr:
            if i + j == 2020:
                return i * j

def day1part2(filename):
    f = open(filename)

    arr = f.read().split()
    f.close()

    arr = np.array(arr, dtype=int)
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == 2020:
                    return i * j * k

print(day1part1("input.txt"))
print(day1part2("input.txt"))