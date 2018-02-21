def charFreq(string):
    '''Counts the frequency of characters in a string'''
    freqDict = {}
    for y in string:
        if not y in freqDict:
            freqDict[y] = 1
        else:
            freqDict[y] += 1
    print(freqDict)

def main():
    charFreq("abcdefghijklmnopqrstuvwxyz")
    charFreq("What is the sound of one hand clapping?")

if __name__ == "__main__":
    main()
