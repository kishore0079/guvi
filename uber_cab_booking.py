a={"mini":10,"micro":20,"auto":30,"share":40}
mini=5
micro=5
auto=5
share=5
availability={"mini":5,"micro":20,"auto":30,"share":40}
print("before bookin",availability)
sp=int(input("enter starting point"))
ep=int(input("enter ending point"))
cab=str(input())
availability[cab]=availability[cab]-1
while(availability[cab]!=0):
    if(availability[cab]!=0):
        cost=ep-sp
        print(cost*a[cab])
    print(availability)
    sp=int(input("enter starting point"))
    ep=int(input("enter ending point"))
    cab=str(input())
    availability[cab]=availability[cab]-1
    print("before bookin",availability)
