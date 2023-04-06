N, M = map(int, input().split())
KS = [list(map(int, input().split())) for _ in range(M)]
K = [ks[0] for ks in KS]
S = [ks[1:] for ks in KS]
P = list(map(int, input().split()))
c = 0

assert len(S) == len(P)
temp=[]
for s in S:
    temp += s
bulb_max_no = max(temp)
for i in range(2**N):  # 全部で ２のｎ乗通りあるのがbit探索
    B = list(map(int, bin(i)[2:].zfill(bulb_max_no)))  # 例えば，1つ目だけon のこりoff
    each_light_state=[]
    #print(B)
    for s,p in zip(S, P):
        each_light_state.append( sum([B[i-1] for i in s]) % 2 == p)
    if all(each_light_state):
        c+=1
print(c)