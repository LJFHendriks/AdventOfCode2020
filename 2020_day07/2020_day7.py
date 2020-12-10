import re

def containrules():
    f = open("input.txt")

    str = f.read()
    f.close()
    arr = str.split("\n")

    rulesdic = {}
    for i in range(len(arr)):
        x = re.findall(r"(\w+\s\w+)\sbag", arr[i])
        for j in range(1,len(x)):
            if x[j] in rulesdic:
                rulesdic[x[j]].append(x[0])
            else:
                rulesdic[x[j]] =[x[0]]
    return rulesdic

def lookupbag(rulesdic, bagcolor):
    if bagcolor in rulesdic:
        bags = rulesdic[bagcolor]
        bagcolors = [bagcolor]
        for i in range(len(bags)):
            newbagcolors = lookupbag(rulesdic,bags[i])
            for i in range(len(newbagcolors)):
                if newbagcolors[i] not in bagcolors:
                    bagcolors.append(newbagcolors[i])
        return bagcolors
    return [bagcolor]

def day7part1(bagcolor):
    rulesdic = containrules()
    return len(lookupbag(rulesdic,bagcolor))-1

def containrules2():
    f = open("input.txt")

    str = f.read()
    f.close()
    arr = str.split("\n")

    rulesdic = {}
    for i in range(len(arr)):
        origbag = re.findall(r"^(\w+\s\w+)\sbag", arr[i])

        bags = re.findall(r"(\d+)\s(\w+\s\w+)\sbag", arr[i])

        tempdic = {}
        for tup in bags:
            tempdic[tup[1]] = int(tup[0])
        rulesdic[origbag[0]] = tempdic
    return rulesdic

def iterbag(rulesdic, bagcolor):
    sum = 0
    for temp in rulesdic[bagcolor]:
        sum += rulesdic[bagcolor][temp] * iterbag(rulesdic,temp)
    return sum+1

def day7part2(bagcolor):
    rulesdic = containrules2()
    return iterbag(rulesdic,bagcolor) - 1


print(f"The number of bags that can contain a shiny gold bag equals: {day7part1('shiny gold')}")
print(f"The number of individual bags inside a shiny gold bag equals: {day7part2('shiny gold')}")
