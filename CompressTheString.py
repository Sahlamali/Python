Given a string S. Suppose a character 'c' occurs consecutively n times in the string. Replace these consecutive occurrences of the character 'c' with (n,c) in the string.

#Program
no = input()
l= len(no)
n=list(no)
a=[]
b=[]
c=1
t=n[0]
for i in range(1,l):
    
    if(t==n[i]):
        c=c+1
    else:
        b=[]
        t=int(t)
        b.append(c)
        b.append(t)
        b=tuple(b)
        a.append(b)
        del(b)
        c=1
        t=n[i]

b=[]
t=int(t)
b.append(c)
b.append(t)
b=tuple(b)
a.append(b)
del(b)
print(*a,sep=" ")   
