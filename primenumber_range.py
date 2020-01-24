n=int(input())
def checkprime(i):
    count=0
    for j in range(1,i):
        if(i%j==0):
            count=count+1
    if(count==1):
        print(i,end=" ")
 
if(n>=1 and n<=100000):
    for i in range(2,n):
        checkprime(i)
