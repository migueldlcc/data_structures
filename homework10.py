def bestMatcher(pattern, text): # Homework #10
    output = []
    for i in range(len(text) - len(pattern) + 1):
        s = text[i:i + len(pattern)] # portion of text starting at position i and look for the character's length
        if s == pattern:
            output.append(i)
    return output


p = "ACATA"
t = "ACGACACATAGTCACTTGGCACATAGTCAGTACCTGAACATACATAGTCAACATA"
v = bestMatcher(p, t)
print(v)
