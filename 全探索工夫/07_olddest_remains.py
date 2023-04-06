## 二つのcoordsの組み合わせのにおける距離の集合を作成
## 距離が2つ → 正四角形．距離が3つ → 長方形
import itertools
import math

with open('input.txt') as f:
    s = f.read()
s = s.split('\n')
n = int(s.pop(0))
S=[]
for i,j,k,l in itertools.combinations(range(n), 4):
    flag=True
    for m, n in itertools.combinations([i,j,k,l],2):
        o, p = [ele for ele in [i,j,k,l] if ele not in [m,n]]
        m,n,o,p = s[m], s[n], s[o], s[p] 
        m,n,o,p = map(lambda x:list(map(int,x)), [m.split(),n.split(),o.split(),p.split()])
        if ((m[0]-n[0])**2 + (m[1]-n[1])**2) == ((o[0]-p[0])**2 + (o[1]-p[1])**2):
            flag+=1
            print((m[0]-n[0])**2 + (m[1]-n[1])**2, (o[0]-p[0])**2 + (o[1]-p[1])**2)
            continue
        else:
            flag=False
    if flag==True:
        #i,j = s[i].split(), s[j]
        print(m,n)
        #S.append((math.sqrt( (m[0]-n[0])**2 + (m[1]-n[1])**2)) ** 2 )
        S.append( (m[0]-n[0])**2 + (m[1]-n[1])**2)

print(max(S))
print(S)
