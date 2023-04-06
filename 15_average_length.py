import itertools
import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
X = [xy[0] for xy in XY]
Y = [xy[1] for xy in XY]

dist_sum=0
for orders in itertools.permutations(range(N)):
    dist=0
    for i in range(N-1):
        dist += math.sqrt( (X[orders[i]]-X[orders[i+1]])**2 + (Y[orders[i]]-Y[orders[i+1]])**2 )
    #print(dist)
    dist_sum += dist
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)
#print(factorial(N))
print(dist_sum/factorial(N))