a=list(map(int,input().split(',')))
for i in a:
     f=1
     for j in range(1,i+1):      
        f=f*j
     print(f,end=',')
