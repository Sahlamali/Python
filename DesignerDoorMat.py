ni=input().split(" ")
m=int(ni[1])
n=int(ni[0])
stick=1
num=1
ran = (n-1)//2
hash_=(m-3)//2
for i in range (0,ran):
    
    stick=1
    for j in range(0,hash_):
       print("-",end="")
    
    while(stick<=num):
        print(".|.",end="")
        stick+=1
    for j in range(0,hash_):
       print("-",end="")
    
    hash_-=3
    print(' ')
    num+=2

for i in range (0,n):
    print("-",end="")
print("WELCOME",end="")
for i in range (0,n):
    print("-",end="")
print(' ')    
num=num-2
hash_=(n-1)//2
for i in range (0,ran):
    
    stick=1
    for j in range(0,hash_):
       print("-",end="")
    
    while(stick<=num):
        print(".|.",end="")
        stick+=1
    for j in range(0,hash_):
       print("-",end="")
    
    hash_+=3
    print(' ')
    num-=2
