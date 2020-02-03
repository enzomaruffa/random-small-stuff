import sys

totalCalls = 0

def ack(m, n):
    global totalCalls
    totalCalls += 1
    print("Calling ack with", m, n) 
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)    
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n-1))
    return 0

m = int(sys.argv[1])
n = int(sys.argv[2])

ack(m, n)
print(totalCalls)


