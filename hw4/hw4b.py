

def parse(s):
    wordList = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    start = 0
    current = 0
    count = 0

    while current < len(s):
        if s[current] in alphabet:
            count += 1
        else:
            if count >= 4:
                word = s[start:current]
                wordList.append(word.strip().lower())
            count = 0
            start = current
        current += 1

    return wordList



def computeWordFrequencies(filename):
     # list of list containing unique words in frequencies
     masterWordList = [[], []] 

     # open file, parse each line
     f = open(filename, 'r')
     s = f.read() # read the file into a string
     lines = s.split('\n')
     for line in lines:
          lineWords = parse(line)
          for word in lineWords:
               index = 0
               inList = False
               while index < len(masterWordList[0]):
                    # if the word is in the list, increment it's freq count
                    if masterWordList[0][index] == word:
                         masterWordList[1][index] += 1
                         inList = True
                         break
                    index += 1
               if inList == False: # if the word is not in list, add it to end
                    masterWordList[0].append(word)
                    masterWordList[1].append(1)
               else:
                    inList = False # reset                              
     f.close()
     return masterWordList
                
        


def test():
     filename = 'test.txt'
     masterWordList = computeWordFrequencies(filename)
     print(masterWordList)


test() 
