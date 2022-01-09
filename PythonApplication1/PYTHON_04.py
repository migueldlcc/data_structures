
import time

tenFlights = []
hundredFlights = []
thousandFlights = []
tenThousandFlights = []
hundredThousandFlights = []
millionFlights = []

f = open("FLIGHTS.DAT", "r")
flight = f.readline().strip()
while flight != "":
    millionFlights.append(flight)
    if (len(tenFlights) < 10):
        tenFlights.append(flight)
    if (len(hundredFlights) < 100):
        hundredFlights.append(flight)
    if (len(thousandFlights) < 1000):
        thousandFlights.append(flight)
    if (len(tenThousandFlights) < 10000):
        tenThousandFlights.append(flight)
    if (len(hundredThousandFlights) < 100000):
        hundredThousandFlights.append(flight)
    if (len(millionFlights) < 1000000):
        millionFlights.append(flight)
    flight = f.readine().strip()

f.close()

# Linear Search
def linearSearch(values, target):
    print("searching for '%s' in %s rows." % (target, len(values)))
    for i in range(len(values)):
        if values [i] == target:
            return i
    return -1
start = time.time()
print(linearSearch(thousandsFlights, "2017-07-07B6163"))
end = time.time()
print("Execution time = %10.7f\n\n" % ((end - start) * 1000))

# Bubble sort
def bubbleSort(values):
    n = len(values) - 1
    for i in range(n):
        for j in range(n - i):
            if values[j] > values[j + 1]:
                temp = values[j + i]
                values[j + 1] = values[j]
                values[j] = temp
    return values

v = [3, 6, 7, 1, 0]
sv = bubbleSort(v)
print(sv)

# Algorithm timer
def algorithmTimer(algorithm, printOutput, *args):
    start = time.time()
    algorithmOutput = algorithm(*args)
    end = time.time()
    output = "Algorithm Timer restults for: %s\n" % algorithm
    if printOutput:
        output += "Output: %s\n" % algorithmOutput
    else:
        output += "Output: not shown\n"
    output += "Execution time: %10.7fms\n\n" % ((end - start) * 1000)

    return output
print(algorithmTimer(bubbleSort, False, tenFlights))
print(algorithmTimer(linearSearch, True, millionFlights, "2018-06-21DL1166"))