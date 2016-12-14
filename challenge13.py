
# f = open('day7.testdata', 'r')
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


def isAbba(word):
    return word[0] == word[3] and word[1] == word[2] and word[0] != word[1]


def findAbba(string):
    if len(string) < 4:
        return ''
    elif isAbba(string[:4]):
        return string[:4]
    else:
        return findAbba(string[1:])


def containsAbba(segment):
    if len(findAbba(segment)) == 0:
        return False
    return True


def containAbba(listOfStrings):
    for string in listOfStrings:
        if containsAbba(string):
            return True
    return False


def findAbbaInList(listOfStrings):
    for string in listOfStrings:
        if containsAbba(string):
            return findAbba(string)
    return ''

counter = 0

for line in f:
    (outside, inside) = segmentsOf(line)
    if containAbba(outside) and not containAbba(inside):
        # print(outside, 'does contain an ABBA and ', inside, 'does not contain an ABBA')
        counter += 1
    if containAbba(inside):
        print(inside, 'this contains an ABBA ', findAbbaInList(inside))

print(counter)
