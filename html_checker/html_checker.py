# Miguel de la Cruz Cabello
# Professor Merritt
# COMS 326
# 21 February 2021

import Stack_adtl


def balanced(string):
    s = Stack_adtl.Stack()
    index = 0
    while index < len(string):
        bal = True
        htmlTag = []
        if string[index] == '<':
            htmlTag.append('<')
            index += 1
            if string[index] == '/':
                bal = False
                index += 1
     
            while (index < len(string) and (string[index].isalpha() or string[index].isdigit())):
                htmlTag.append(string[index])
                index += 1
          
            htmlTag.append(string[index])
            tag = ''.join(htmlTag)
           
            if bal:
                s.push(tag)
            elif s.isEmpty():
                return False
            else:
                topBal = s.pop()
                if topBal != tag:
                    return False
        index += 1
    if s.isEmpty():
        return True
    return False
 
##def balanced(string):
##    s = ADT.Stack()
##    bal = True
##    index = 0
##    while index < len(string) and bal:
##        tagStart = string.find("<", index) + 1
##        tagEnd = string.find(">", tagStart)
##        tag = string[tagStart:tagEnd] if tagEnd > tagStart else ""
##
##        if tag in { "html", "head", "title", "body", "h1", "a"}:
##            s.push(tag)
##        else:
##            if s.isEmpty():
##                bal = False
##            else:
##                top = s.pop()
##                bal = (top == "html" and tag == "/html") \
##                      or (top == "head" and tag == "/head") \
##                      or (top == "title" and tag == "/title") \
##                      or (top == "body" and tag == "/body") \
##                      or (top == "h1" and tag == "/h1") \
##                      or (top == "a" and tag == "a") \
##        index = tagEnd +1
##
##    if bal and s.isEmpty():
##        return True
##    else:
##        return False
    
s = "<html></html>"
g = "<body>My Website<body>"
k = "<html><head><title>Example</title></head><body><h1>Hello, world</h1></body></html<"
a = "<html> <head> <title> Example </title> </head>"
b = "<html> <head> <title> Example </title> </head> </html>"
print ("Is tag s valid?")
print(balanced(s))
print ("Is tag g valid?")
print (balanced(g))
print ("Is tag k valid?")
print(balanced(k))
print ("Is tag a valid?")
print (balanced(a))
print ("Is tag b valid?")
print (balanced(b))

