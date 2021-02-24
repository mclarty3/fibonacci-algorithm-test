import math
from time import perf_counter_ns
import matplotlib.pyplot as plt

def recursiveFib(n):
    # I decided to have n start at 0 for consistency with the other algorithms. F(1) = 1, F(2) = 1, F(3) = 2, etc.
    if n > 2:
        return recursiveFib(n - 2) + recursiveFib(n - 1)
    else:
        return 1

def explicitFib(n):
    return math.floor(((((1 + math.sqrt(5)) / 2) ** n) - (((1 - math.sqrt(5)) / 2) ** n)) / math.sqrt(5))

def loopFib(n):
    count = 0
    n1, n2 = 0, 1
    while count < n:
        nth = n1 + n2
        n1, n2 = n2, nth
        count += 1
    return n1

def matrixMultFib(n):
    # I copied this code from Stack Overflow; thanks Piotr Dabkwoski!

    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

def testFib(n, recursive=True):
    # Tests runtimes for each algorithm calculating the nth digit of the Fibonacci sequence
    # The recursive parameter determines whether or not the recursive algorithm will be run
    # This was implemented as it begins to take infeasibly long around n = 40

    ret = {}

    if recursive:
        timer1 = perf_counter_ns()
        ret["Recursive"] = [recursiveFib(n), perf_counter_ns() - timer1]

    timer2 = perf_counter_ns()
    ret["Explicit"] = [explicitFib(n), perf_counter_ns() - timer2]

    timer3 = perf_counter_ns()
    ret["Loop"] = [loopFib(n), perf_counter_ns() - timer3]

    timer4 = perf_counter_ns()
    ret["Matrix"] = [matrixMultFib(n), perf_counter_ns() - timer4]
    
    return ret

def testFibPrint(n, recursive=True):
    # Prints the results of one test run of each algorithm and the amount of time it took to calculate F(n)

    ret = testFib(n, recursive)

    if recursive:
        print("Recursive: " + str(ret["Recursive"][0]) + " took " + str(ret["Recursive"][1]) + " nanoseconds")
        
    print("Explicit: " + str(ret["Explicit"][0]) + " took " + str(ret["Explicit"][1]) + " nanoseconds")
    print("Loop: " + str(ret["Loop"][0]) + " took " + str(ret["Loop"][1]) + " nanoseconds")
    print("Matrix: " + str(ret["Matrix"][0]) + " took " + str(ret["Matrix"][1]) + " nanoseconds")

print("Calculating fibonacci sequence...")
recursivePoints, loopPoints, explicitPoints, matrixPoints = [], [], [], []
for i in range(1, 1475):
    points = []
    if (i < 17):
        points = testFib(i)
        recursivePoints.append((i, points["Recursive"][1]))
    else:
        points = testFib(i, False)
    loopPoints.append([i, points["Loop"][1]])
    explicitPoints.append([i, points["Explicit"][1]])
    matrixPoints.append([i, points["Matrix"][1]])

# I wrote this to exclude ridiculous outliers in the data (I'm not sure what causes the random spikes, I guess other stuff happening on the CPU?)
# I think I prefer to accurately represent the data however, so I'm commenting it out for now
""" for arr in [loopPoints, explicitPoints, matrixPoints]:
    for i in range(1, len(arr)):
        print(i)
        if arr[i][1] > (arr[i-1][1] * 5):
            arr[i][1] = arr[i-1][1] """

print("Plotting...")

plt.title("Time for algorithms to calculate F(n)")
plt.xlabel('n')
plt.ylabel('Time (ns)')

plt.plot([a[0] for a in recursivePoints], [a[1] for a in recursivePoints], "b-")
plt.plot([a[0] for a in loopPoints], [a[1] for a in loopPoints], "r-")
plt.plot([a[0] for a in explicitPoints], [a[1] for a in explicitPoints], "y-")
plt.plot([a[0] for a in matrixPoints], [a[1] for a in matrixPoints], "g-")

plt.text(recursivePoints[-1][0], recursivePoints[-1][1], 'Recursive')
plt.text(loopPoints[-1][0],  loopPoints[-1][1], 'Loop')
plt.text(explicitPoints[-1][0], explicitPoints[-1][1], 'Explicit')
plt.text(matrixPoints[-1][0], matrixPoints[-1][1], 'Matrix')

plt.show()