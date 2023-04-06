# 3Clen(S)だとTLE
# 相性番号を作成できるかで判断 1000*30000 最悪
import joblib

N = input()
S = input()
S = list(map(int, list(S)))

def solve(i):
    global COUNT
    flag = False
    if len(str(i)) == 1:
        i = ['0','0',str(i)]
    elif len(str(i)) == 2:
        i = ['0'] + list(str(i))
    else:
        i = list(str(i))
        #print('##',i)
    idx=0
    #print(i)
    i = list(map(int, i))
    for s in S:
        #print(s, i[idx])
        if s==i[idx]:
            idx += 1
            if idx == 3:
                flag = True
                break
    if flag == True:
        #print('here')
        return 1
    return 0

count = joblib.Parallel(n_jobs=-1)([joblib.delayed(solve)(i) for i in range(1000)])
print(sum(count))