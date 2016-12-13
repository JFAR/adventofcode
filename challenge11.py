

f = open('day6.data', 'r')

message = [{}, {}, {}, {}, {}, {}, {}, {}]

for line in f:
    for i in range(8):
        char = line[i]
        if line[i] in list(message[i]):
            message[i][char] += 1
        else:
            message[i][char] = 1


def getMostCommonLetter(frequency):
    print(frequency)
    maximum = 0
    for char in list(frequency):
        if frequency[char] > maximum:
            output = char
            maximum = frequency[char]

    return output

print(''.join([getMostCommonLetter(x) for x in message]))
