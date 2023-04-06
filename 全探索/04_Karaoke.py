N, M = map(int, input().split())
A=[]
for i in range(N):
    A.append(list(map(int, input().split())))
    
sum=0
max_sum=0
for i in range(M-1):
    for j in range(i+1,M):
        for a in A:
            a = max(a[i],a[j])
            sum+=a
        max_sum = max(max_sum, sum)
        sum=0
print(max_sum)