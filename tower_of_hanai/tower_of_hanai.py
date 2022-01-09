call = 1
index = "a"

def moveDisk(fromPeg, toPeg):
    global call 
    global index
    print("(call #%03d%s) moving disk %d from %d" % (fromPeg, toPeg))
    call += 1

def moveTower(height, fromPeg, toPeg, usingPeg):
    global index
    if height > 0:
        index = "a"
        moveTower(height - 1, fromPeg, usingPeg, toPeg)
        moveDisk(fromPeg, toPeg)
        moveTower(height - 1, usingPeg, toPeg, fromPeg)

moveTower(4, 2, 1, 3)
    
