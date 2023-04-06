n, m = map(int, input().split())
K, S = [0]*m, [[]]*m
for i in range(m):
    K[i], *S[i] = map(int, input().split())
P = list(map(int, input().split()))
c = 0
for l in range(2**n):
    B = list(bin(l)[2:].zfill(n))
    if all(sum(int(B[s-1]) for s in S[i]) % 2 == P[i] for i in range(m)):
        c += 1
        print(B)
print(c)