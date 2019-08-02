a = input("Enter the string:")
c = input("Enter the set of characters to be replaced:")
d=input("Enter the replaced set of characters:")
string=list(a)
word=[]
#string.append(a)
word.append(c)
#print(a)
#print(word)
w = len(c)
l = len(a)-w+1
for i in range(0,l):
      #print(a[i:w])
      if(a[i:w+i]==c[:]):
          string[i:w+i]=d[:]
print("The string after replacment is:",end=" ")
print(*string,sep="")
