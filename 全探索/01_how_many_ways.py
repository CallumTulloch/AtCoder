while(1):
    n,x = map(int, input().split())
    if n==0 and x==0:
        break
    c=0
    for i in range(1,n):          # 例えば n=10     -> 1,2,3,4,5,6,7,8,9
        for j in range(i+1,n+1):  # 例えば n=10,i=5 -> 6,7,8,9,10
            k = x-i-j
            if k > j:
                print(i,j,k)
                c+=1
    print(c)