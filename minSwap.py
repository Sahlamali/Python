#You are given an unordered array consisting of consecutive integers E [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

#Input Format
#The first line contains an integer,n , the size of arr . 
#The second line contains n space-separated integers arr[i].

#Output Format
#Return the minimum number of swaps to sort the given array.

#Program
def minimumSwaps(arr):
    l=len(arr)
    swap=0
    for i in range(0,l):
        if (i+1)!=arr[i]:
            j=arr.index(i+1)
            swap=swap+1
            arr[j],arr[i] = arr[i],arr[j]
            #arr[i]=i+1
    return swap
n = int(input())
arr = list(map(int, input().rstrip().split()))
res = minimumSwaps(arr)
print(res)
