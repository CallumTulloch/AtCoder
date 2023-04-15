import numpy as np
np.set_printoptions(threshold=1000, linewidth=10000) # 要素の数，横幅

n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
A_max = 2000 + 1

dp = np.zeros(A_max*len(A)).reshape(len(A), A_max)
for i in range(n):
    a = A[i]
    if i==0:
        dp[i][0] = 1
        dp[i][a] = 1
        continue
    for j in range(A_max):
        if (j-a) >= 0 and dp[i-1][j-a] == 1:
            dp[i][j] = 1
        if dp[i-1][j] == 1:
            dp[i][j] = 1

for m in M:
    if dp[-1][m] == 1:
        if dp[-1][m] == 1:
            if dp[-1][m] == 1:
            print('yes')
    else:
        print('no')
