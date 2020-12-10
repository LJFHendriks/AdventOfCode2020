key = {
    "F": 0,
    "B": 1,
    "L": 0,
    "R": 1
}

def seat2rowcol(seat,rows,cols):
    row = 0;
    for i in range(rows):
        row += key[seat[i]]*2**(rows-1-i)

    col = 0
    for i in range(cols):
        col += key[seat[rows+i]]*2**(cols-1-i)
    return row, col

def day5part1():
    f = open("input.txt")

    str = f.read()
    f.close()

    arr = str.split()

    maxseatID = 0;
    for i in range(len(arr)):
        row , col = seat2rowcol(arr[i],7,3)

        seatID = row*8+col
        if seatID > maxseatID:
            maxseatID = seatID


    return maxseatID

def day5part2():
    f = open("input.txt")

    str = f.read()
    f.close()

    arr = str.split()

    seatIDarr = []

    for i in range(len(arr)):
        row , col = seat2rowcol(arr[i],7,3)
        seatIDarr.append(row*8+col)

    for i in range(1,max(seatIDarr)-1):
        if i not in seatIDarr:
            if i + 1 in seatIDarr and i - 1 in seatIDarr:
                return i
    return 0



print(f"The highest seatID equals: {day5part1()}")
print(f"The seatID of my seat equals: {day5part2()}")
