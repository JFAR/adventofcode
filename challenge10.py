import hashlib

# doorId = 'abc'
doorId = 'cxdnnyjw'


def encodedHash(doorId, counter):
    m = hashlib.md5()
    m.update(str.encode(doorId + str(counter)))
    return m.hexdigest()


def printInterestingHexes(doorId):
    counter = 0
    passwordLength = 0
    password = list('________')
    while passwordLength < 8:
        encoded = encodedHash(doorId, counter)
        if encoded[:5] == '00000':
            position = encoded[5]
            if position in ['0', '1', '2', '3', '4', '5', '6', '7'] and password[int(position)] == '_':
                password[int(position)] = encoded[6]
                passwordLength += 1
        counter += 1
        print(''.join(password))

encoded = encodedHash(doorId, 3231929)
# print(doorId + str(3231929) + " " + encoded[5] + " " + encoded)
# print()

printInterestingHexes(doorId)
