#Given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.

n = int(input())
array = []
for i in range(0,n):
    array.append(input())
a = list(dict.fromkeys(array))
l=len(a)
print(l)
for i in a:
    k=i
    count=0
    for j in array:
        if(k==j):
            count+=1
    print(count,end=" ")
