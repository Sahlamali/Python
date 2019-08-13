#Given a string S , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

#Print the three most common characters along with their occurrence count.
#Sort in descending order of occurrence count.
#If the occurrence count is the same, sort the characters in alphabetical order.

#Sample Input 0
#aabbbccde

#Sample Output 0
#b 3
#a 2
#c 2

#Program

if __name__ == '__main__':
    s = input()
    m = list(s)
    a={}
    l=[]
    g=[]
    h=[]
    b={}
    #print(m)
    n= list(dict.fromkeys(m))
    a = dict.fromkeys(m)
    #print(n)
    ni = len(n)
    for i in n:
        c=0
        for j in m:
            if i==j:
                c+=1
        a[i]=c
   
    a=sorted(a.items(), key = lambda kv:(kv[0]))
    g=dict(a)
    g=sorted(g.items(), key = lambda kv:(kv[1]),reverse=True)
    s=0
    for key,value in g:
        if s<3:
            print (key,value)
            s+=1
        else:
            break
   
