# ピザはAとBを合わせた金額と，C2枚の金額の差によってどちらを買うべきか決める．→ AとB小さいほうの数にとりあえず合わせる
# 片方のピザを揃えるときに，c2枚を買うか，片方のピザのみ買うかは小さいほうを選ぶ．
A, B, C, X, Y = map(int, input().split())
sums=[]
#print('inter',inter_opt)

if A+B >= 2*C:
    inter_opt = 2*C*min(X,Y)
    if(X >= Y):
        for a in range(X-Y+1):
            sum = A*a + 2*C*(X-Y-a)
            #print(A,a,'+ 2',C,'(',X,'-',a)
            #print(sum)
            sums.append(sum)
    else:
        for b in range(Y-X+1):
            sum = B*b + 2*C*(Y-X-b)
            sums.append(sum)
    print(min(sums)+inter_opt)
    #print(sums)

else:
    sum = A*X + B*Y
    print(sum)