def checkPalindrome(inputString):

    InvertedString = inputString[::-1]
    MiddleLine = len(inputString) // 2
    LongFirstPart = inputString[0:MiddleLine:
    #LongSecondPart = inputString[MiddleLine::-1]
    LongSecondPart = InvertedString[0:MiddleLine:]
    print(len(inputString))
    print(InvertedString)
    print(MiddleLine)
    print(LongFirstPart, LongSecondPart)
    return print(LongFirstPart == LongSecondPart)


checkPalindrome('hlbeeykoqqqqokyeeblh')