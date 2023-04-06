## 客の商品の位置の間隔によって候補を絞る解答(全通りよりは早く終わる)
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
A = [ab[0] for ab in AB]
B = [ab[1] for ab in AB]
minimun = min(A)
maximum = max(B)
dis_sum=[]
AB_sumd = [sum(A), sum(B)]
for ent in range(minimun, maximum-minimun+1):   # a : minimun ~ maximum
    for exit in range(ent, maximum+1):     # b : a   ~ maximum
        temp=[]
        #for a, b in AB:
        #    dis = abs(ent - a) + (b - a) + abs(exit - b)
        #    #print(a,b,dis)
        #    temp.append(dis)
        #dis_sum.append(sum(temp))
        dis_sum.append()
#print(sum)
print(min(dis_sum))


## 入口と出口はいづれかの客の商品の位置であることを見敗れた場合以下のコード
## 答えから解答を絞る
n=int(input())
a=[0]*n
b=[0]*n
ans=0
sum=0
for i in range(n):
    a[i],b[i]=map(int,input().split())
    #ans=max(ans,max(a[i],b[i]))
for i in range(n):      # 入口
    for j in range(n):  # 出口
        sum=0
        #入口がa[i]マス出口がb[j]マス
        for k in range(n):
            #|a[i]-a[k]|+|a[k]-b[k]|+|b[k]-b[j]|
            sum+=abs(a[i]-a[k])+abs(a[k]-b[k])+abs(b[k]-b[j])
        print(f'{i}({a[i]}),{j}({b[i]}),{k}({a[k]}),{sum}')
        ans=min(ans,sum)
        if i+j==0:
            ans=sum
print(ans)