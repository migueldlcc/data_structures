p = "ACATA"
t = "ACGACACATAGTCACTTGGCACATAGTCAGTACCTGAACATACATAGTCAACATA"

def simpleMatcher(pattern, text):
    starti = 0 # keeps track where a pattern starts to match
    i = 0 # index value as it reads across the text 
    j = 0 # index of the pattern
    match = False
    stop = False
    # The boolean values keep the while loop running until nothing is found
    while not match and not stop:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            starti += 1 # start looking at the next character
            i = starti
            j = 0 # reset to 0
        if j == len(pattern):
            match = True
        else: 
            if i == len(text): # if pattern did not match and we reach the end of out text
                stop = True
    if match :
        return i - j
    else:
        return -1 # return value whenever a match is not found


def betterMatcher(pattern, text):
    for i in range(len(text) - len(pattern) + 1):
        s = text[i:i + len(pattern)] # portion of text starting at position i and look for the character's length
        if s == pattern:
            return i
    return -1

def bestMatcher(pattern, text): # Homework #10
    output = []
    for i in range(len(text) - len(pattern) + 1):
        s = text[i:i + len(pattern)] # portion of text starting at position i and look for the character's length
        if s == pattern:
            output.append(i)
    return output

v = bestMatcher(p, t)
print(v)
