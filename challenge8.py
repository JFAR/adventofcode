def convertToList(filehandle):
  print('converting file to list')
  for line in filehandle:
    calculatedChecksum = checkSumOf(line)
    checksumPart = getCheckSumPartOf(line)
    ID = idOf(line)
    if calculatedChecksum == checksumPart:
      decodedMessage = decode(line, int(ID) % 26)
      if decodedMessage[:5]=='north':
        print(decodedMessage)
        print(ID)

def decode(line, key):
  output = line.split('-')[:-1]
  output = [decodeBlock(x, key) for x in output]
  return ' '.join(output)

def decodeBlock(block, key):
  return ''.join([decodeCharacter(x, key) for x in block])

decoder = {'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}

def decodeCharacter(character, key):
  currentCharacter = character
  for i in range(key):
    currentCharacter = decoder[currentCharacter]
  return currentCharacter

def idOf(entry):
  return entry.split('-')[-1].split('[')[0]

def checkSumOf(entry):
  chunks = ''.join(entry.split('-')[:-1])
  letters = {}
  for character in chunks:
    if character in list(letters):
      letters[character] += 1
    else:
      letters[character] = 1
  output = ''.join(sortedListOf(letters)[:5])
  return output

def sortedListOf(letters):
  output = []
  for letter in list(letters):
    output = insertLetterInto(output, letter, letters)
  return output

def insertLetterInto(listOfLetters, letterToInsert, letters):
  count = 0
  for letter in listOfLetters:
    if (letters[letter] < letters[letterToInsert] or ((letters[letter] == letters[letterToInsert]) and (letter > letterToInsert))):
      return list(''.join(listOfLetters[:count]) + letterToInsert + ''.join(listOfLetters[count:]))
    count+=1
  if count ==0:
    return [letterToInsert]
  else:
    listOfLetters.append(letterToInsert)
    return listOfLetters

def getCheckSumPartOf(entry):
  output = entry.split('[')[1].split(']')[0]
  return output

def main():
  datafile = open('day4.data', 'r')
  print('start')
  output = convertToList(datafile)
  print('fin')

if __name__ == '__main__':
  main()
