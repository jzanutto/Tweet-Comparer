def BuildDictionary(dictionaryFile):
    dictionary = open(dictionaryFile, "r")
    validWords = set()

    for word in dictionary:
        validWords.add(word.lower())

    return list(validWords)