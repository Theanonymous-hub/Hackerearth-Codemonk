t=int(input())
while t!=0:
    n=int(input())

    m=[]
    for i in range(n):
        m.append(list(map(int, input().split())))

    c=0
    for i in range(n):
        for j in range(n):
            for u in range(i, n):
                for k in range(j, n):
                    if m[i][j]>m[u][k]:
                        c+=1
                        
    print(c)
    t-=1
    
