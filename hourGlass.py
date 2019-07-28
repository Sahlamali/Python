 #Program that calculates the hourglass sum for every hourglass in the array h , then print the maximum hourglass sum.
 
 h=[]
for _ in range(0,6):
    h.append(list(map(int, input().rstrip().split())))
#print(h)
c=0
total=[]
for i in range(0,4):
    for j in range(0,4):
        c= h[i][j]+h[i][j+1]+h[i][j+2]+h[i+1][j+1]
        c = c+h[i+2][j]+h[i+2][j+1]+h[i+2][j+2]
        total.append(c)
print(max(total))
