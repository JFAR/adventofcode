
# f = open('day7.testdata2', 'r')
f = open('day7.data', 'r')


def segmentsOf(line):
    outside = []
    inside = []
    output = ''

    for character in line[:-1]:
        if character == '[':
            outside.append(output)
            output = ''
        elif character == ']':
            inside.append(output)
            output = ''
        else:
            output += character

    outside.append(output)
    return [outside, inside]


def isAba(word):
    return word[0] == word[2] and word[0] != word[1]


def findAba(string, listOfAbas):
    if len(string) < 3:
        return listOfAbas
    elif isAba(string[:3]):
        listOfAbas.append(string[:3])
        return findAba(string[1:], listOfAbas)
    else:
        return findAba(string[1:], listOfAbas)


def containsAba(segment):
    if len(findAba(segment, [])) == 0:
        return False
    return True


def containAba(listOfStrings):
    for string in listOfStrings:
        if containsAba(string):
            return True
    return False


def findAbaInList(listOfStrings):
    listOfAbas = []
    for string in listOfStrings:
        if containsAba(string):
            listOfAbas.extend(findAba(string, []))
    return listOfAbas


def hasMatch(list1, list2):
    print(list1, list2)
    for item in list1:
        if invert(item) in list2:
            return True
    return False


def invert(aba):
    return aba[1] + aba[0] + aba[1]

counter = 0

for line in f:
    (outside, inside) = segmentsOf(line)
    if hasMatch(findAbaInList(outside), findAbaInList(inside)):
        counter += 1

print(counter)
