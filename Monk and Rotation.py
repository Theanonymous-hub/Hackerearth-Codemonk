#Rotate an integer with 2 times

t=int(input())
while t!=0:
    n,k = map(int,input().split())
    arr=list(map(int,input().split()))
    index=n-(k%n)
    for i in range(index,n):
        print(arr[i], end=" ")
    for i in range(index):
        print(arr[i], end=" ")       

    print(" ")
    t-=1
    
    
    #Input
#1
#5 2
#1 2 3 4 5

#Output
#4 5 1 2 3
#Expected Correct Output
#4 5 1 2 3
    
