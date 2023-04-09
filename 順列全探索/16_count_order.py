import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

#func_power = lambda x:x*1 if x==1 else x*func_power(x-1)
#
#P_sum=0
#for i,n in enumerate(P):
#    if N-i-1 != 0:
#        print(n-1, N-i-1, (n-1) * func_power(N-i-1))
#        P_sum += (n-1) * func_power(N-i-1)
#print('###')
#Q_sum=0
#for i,n in enumerate(Q):
#    if N-i-1 != 0:
#        print(n-1, N-i-1, (n-1) * func_power(N-i-1))
#        Q_sum += (n-1) * func_power(N-i-1)
#print(P_sum, Q_sum)
#print(abs(P_sum-Q_sum))

for i, p in enumerate(itertools.permutations(range(1,N+1))):
    #print(p, P)
    if p == P:
        p_idx = i+1

for i, q in enumerate(itertools.permutations(range(1,N+1))):
    if q == Q:
        q_idx = i+1

print(abs(p_idx-q_idx))