def decodeString(s):
    numbers = []
    chars = []
    for letter in s:
        if letter.isnumeric():
            numbers.append(letter)
        elif letter.isalpha() or letter == "[":
            chars.append(letter)
        elif letter == "]":
            decode = ""
            while chars[-1] != "[":
                decode += chars.pop()
            # remove "["
            chars.pop()
            repeat = int(numbers.pop())
            decode = decode * repeat
            # reverse the string because of the LIFO order
            chars.append(decode[::-1])
    return chars.pop()