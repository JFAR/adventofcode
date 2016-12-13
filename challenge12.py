

f = open('day6.data', 'r')

message = [{}, {}, {}, {}, {}, {}, {}, {}]

for line in f:
    for i in range(8):
        char = line[i]
        if line[i] in list(message[i]):
            message[i][char] += 1
        else:
            message[i][char] = 1


def getLeastCommonLetter(frequency):
    output = list(frequency)[0]
    for char in list(frequency):
        if frequency[char] < frequency[output]:
            output = char

    return output

print(''.join([getLeastCommonLetter(x) for x in message]))
