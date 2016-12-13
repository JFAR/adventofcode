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
    password = '________'
    while passwordLength < 8:
        encoded = encodedHash(doorId, counter)
        if encoded[:5] == '00000':
            if encoded[5] in ['0', '1', '2', '3', '4', '5', '6', '7'] and password[int(encoded[5])] == '_':
                password[int(encoded)] = encoded[6]
                print(password)
                # print(doorId + str(counter) + " " + encoded[5:6] + " " + encoded)
                passwordLength += 1
        counter += 1

encoded = encodedHash(doorId, 3231929)
# print(doorId + str(3231929) + " " + encoded[5] + " " + encoded)
# print()

printInterestingHexes(doorId)
