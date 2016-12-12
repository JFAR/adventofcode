

def convertToList(filehandle):
  print('converting file to list')
  output = 0
  for line in filehandle:
    calculatedChecksum = checkSumOf(line)
    checksumPart = getCheckSumPartOf(line)
    ID = idOf(line)
    print(calculatedChecksum + ' ' + checksumPart + ' ' + ID)
    if calculatedChecksum == checksumPart:
      output += int(ID)
  return output

def idOf(entry):
  return entry.split('-')[-1].split('[')[0]

def checkSumOf(entry):
  chunks = ''.join(entry.split('-')[:-1])
  print(chunks)
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
    print(''.join(output))
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
  print(output)
  print('fin')

if __name__ == '__main__':
  main()
