#Program to find the first runnerup

#input format:
#5
#3 4 5 2 2

#Output
#4

#PROGRAM
arr=[]
n = int(input())
arr = input().split()
a = set(arr)
array = list(a)
l=len(array)
for i in range(0,l):
        for j in range(0,l-1):
            if (int(array[j])>int(array[j+1])):
                t=array[j]
                array[j]=array[j+1]
                array[j+1]=t
print(array)
