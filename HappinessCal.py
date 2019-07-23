#There is an array of n integers. There are also 2 disjoint sets,A  and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B . Your initial happiness is 0 . For each i integer in the array, if iEA , you add +1 to your happiness. If iEB, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
# Program
s= input()
l= s.split(" ")
n=l[0]
m=l[1]
array=[]
a=[]
b=[]
array = input().split(" ")
a = set(input().split(" "))
b = set(input().split(" "))
h =0
for i in array:
    h= int(i in a)+h
    h= h- int(i in b)
print(h)
