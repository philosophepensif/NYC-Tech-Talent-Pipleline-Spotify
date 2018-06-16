def sortByStrings(s, t):
    #construct frequency count
    frequency = {}
    output = ""
    for letter in s:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    print(frequency)
    #traverse pattern and add if letter is in original string, add it to output with same number of occurences in original string
    for pattern_letter in t:
        if pattern_letter in frequency:
            output += pattern_letter * frequency[pattern_letter]
    return output