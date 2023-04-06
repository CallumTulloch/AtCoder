## このやり方は，全員が知り合いではなくて，誰が一番知り合いが多いかを求めてしまっている．
#N, M = map(int, input().split())
#XY = [list(map(int, input().split())) for _ in range(M)]
#
#Xs_relation = [[] for _ in range(N)]   # このように作成しないと参照になっている
#for xy in XY:
#    print(xy)
#    Xs_relation[xy[0]-1].append(xy)
#    Xs_relation[xy[1]-1].append([xy[1],xy[0]])
#    print(Xs_relation)
#
#print(Xs_relation)
#Xs_relation = list(map(lambda x:len(x), Xs_relation))
#print(Xs_relation)
#print(max(Xs_relation)+1)



N, M = map(int, input().split())
relations = [tuple(map(int, input().split())) for _ in range(M)]

ans = 0
for i in range(1 << N): # 2**N より高速. 3<<3 -> 3*2**3．1 << 5 -> 1 * 2**3
    #members = [j for j in range(N) if i & (1 << j)]
    members = [i for i,flag in enumerate( list(map(int, bin(i)[2:].zfill(N))) ) if flag==1]
    print(members)
    flag = True
    for j in range(len(members)):
        for k in range(j+1, len(members)):
            if not ((members[j]+1, members[k]+1) in relations or (members[k]+1, members[j]+1) in relations):
                flag = False
                break
        if not flag:
            break
    if flag:
        ans = max(ans, len(members))
print(ans)

"""
このコードは、Bit探索を用いて、すべての派閥の可能性を列挙して、条件を満たすものの中で最大のものを求めます。
具体的には、i を 0 から 2^N-1 までの整数で走らせ、i を2進数表記した時に 1 となっている桁に対応する議員を集め、それらの人が全員知り合いである場合に派閥とみなしています。
全員が知り合いであるかどうかは、与えられた人間関係のリストを総当たりして調べています。
"""