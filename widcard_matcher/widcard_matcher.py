def wildcardMatcher(pattern, text):
    while "%%" in pattern:
        pattern = pattern.replace("%%", "%")
    segments = pattern.split('%') # Split the pattern into list of segments
    map = dict.fromkeys(segments, None) # Creates a dict that has an element for each of the elements that have a segment splitted by the percent sign

    for segment in segments: # Find location for each segemnt in out text
        temp = []
        for i in range(len(text) - lent(segment) + 1):
            s = text[i:i + len(segment)]
            if s == segment:
                temp.append(i)
        map[segment] = temp # Sets the value
    for k in range(len(segments) - 1, 0, -1): # Check the last segment first, the the next last, until it reaches the first segemtns. It goes backwards.
        segment = segments[k]
        maxPos = -1 if map[segment] == None else map[segment][len(map[segment]) - 1] # Finds the max pos in that segment
        map[segments[k - 1]] = [x for x in map[segments[k - 1]] if x < maxPos]
    return map[segments[0]]

p = "AC%A%TA"
text = "ACGACACATAGTCACTTGGCACATAGTCAGTACCTGAACATACATAGTCAACATA"
#t = "ACAC"
#p = "AC"
text = "CATBATHATRATSAT"
P = "T%%%AT"
