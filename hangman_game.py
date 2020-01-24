s=str(input())
l=[]
k=[]
for i in s:
    l.append(i)
    k.append(i)
m=[]
def guess():
    for y in range(0,len(l)):
        m.append("_")
    print(m)
    i=1
    while(i<=len(s)):
        a=str(input())
        if(a in l):
            n=l.index(a)
            l[n]="0"
            while(m[n]=="_"):
                m[n]=a
        print(m)
        i=i+1
        
guess();
if(m==k):
    print("win")
else:
    print("lost")

