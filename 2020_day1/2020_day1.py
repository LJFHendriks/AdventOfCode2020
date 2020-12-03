import numpy as np

def day1part1(filename):
    f = open(filename)


    arr = f.read().split()
    arr = np.array(arr)
    arr = arr.astype(int)
    for i in arr:
        for j in arr:
            if i + j == 2020:
                return i * j

def day1part2(filename):
    f = open(filename)


    arr = f.read().split()
    arr = np.array(arr)
    arr = arr.astype(int)
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == 2020:
                    return i * j * k

print(day1part1("2020_day1_input.txt"))
print(day1part2("2020_day1_input.txt"))