# 約数は1も自分も入れてよい
N = int(input())
enu_num=0

for n in range(1,1+N):
    if n%2==1:
        yaku_num=0
        for x in range(1,n+1):
            if n%x==0:
                yaku_num+=1
        if(yaku_num == 8):
            enu_num+=1

print(enu_num)