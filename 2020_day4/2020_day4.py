from functools import partial

def day4part1():
    f = open("input.txt")

    str = f.read()
    f.close()

    arr = str.split("\n\n")

    validpass = 0;
    for i in range(len(arr)):
        if allData(arr[i]):
            validpass += 1
    return validpass

def allData(pas):
    if "byr:" in pas:
        if "iyr:" in pas:
            if "eyr:" in pas:
                if "hgt:" in pas:
                    if "hcl:" in pas:
                        if "ecl:" in pas:
                            if "pid:" in pas:
                                return True
    return False


def day4part2():
    f = open("input.txt")

    str = f.read()
    f.close()

    arr = str.split("\n\n")

    validpass = 0;
    for i in range(len(arr)):
        if isValidPass(arr[i]):
            validpass += 1
    return validpass

def year(lower,upper,value):
    if len(value) == 4:
        value = int(value)
        if value >= lower:
            if value <= upper:
                return True
    return False

def hgt(value):
    if value[-2:] == "cm":
        value = int(value[:-2])
        if value >= 150:
            if value <= 193:
                return True
    elif value[-2:] == "in":
        value = int(value[:-2])
        if value >= 59:
            if value <= 76:
                return True
    return False

def hcl(value):
    if value[0] == "#":
        if len(value[1:]) == 6:
            for i in range(1,7):
                if not value[i] in "0123456789abcdef":
                    return False
            return True
    return False

def ecl(value):
    if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False

def pid(value):
    if len(value) == 9:
        if value.isdigit():
            return True
    return False

def error(pas):
    raise Exception("Unknown identifier.")

def isValidPass(pas):
    if allData(pas):
        pas = pas.split()
        switcher = {
            "byr:": partial(year,1920,2002),
            "iyr:": partial(year,2010,2020),
            "eyr:": partial(year,2020,2030),
            "hgt:": hgt,
            "hcl:": hcl,
            "ecl:": ecl,
            "pid:": pid,
            "cid:": lambda pas: True
        }
        for i in range(len(pas)):
            func = switcher.get(pas[i][:4],error)
            if not func(pas[i][4:]):
                return False
        return True
    return False




print(f"The number of valid passwords in task 1 equals: {day4part1()}")
print(f"The number of valid passwords in task 2 equals: {day4part2()}")
