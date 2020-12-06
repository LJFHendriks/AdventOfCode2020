def union(ansarr):
    uniarr = ansarr[0]
    for i in range(1,len(ansarr)):
        for j in range(len(ansarr[i])):
            if ansarr[i][j] not in uniarr:
                uniarr += ansarr[i][j]
    return uniarr

def day6part1():
    f = open("input.txt")

    str = f.read()
    f.close()

    arr = str.split("\n\n")

    sum = 0
    for i in range(len(arr)):
        sum += len(union(arr[i].split()))
    return sum

def intersection(ansarr):
    uniarr = ansarr[0]
    for i in range(1,len(ansarr)):
        newuniarr = ""
        for j in range(len(ansarr[i])):

            if ansarr[i][j] in uniarr:
                newuniarr += ansarr[i][j]

        uniarr = newuniarr
    return uniarr

def day6part2():
    f = open("input.txt")

    str = f.read()
    f.close()

    arr = str.split("\n\n")

    sum = 0
    for i in range(len(arr)):
        sum += len(intersection(arr[i].split()))
    return sum



print(f"The sum of all \"yes\" answered questions equals: {day6part1()}")
print(f"The sum of questions to which everyone answered \"yes\" equals: {day6part2()}")
