#Given q queries. After each query, you need to report the size of the largest friend circle (the largest group of friends) formed after considering that query.

#Input Format
#The first line contains an integer,q , the number of queries to process. 
#Each of the next q lines consists of two space-separated integers denoting the 2-D array queries.

#Output Format
#Return an integer array of size q , whose value at index i is the size of largest group present after processing the ith query.

#Program

def maxCircle(q):
    l =len(q)
    c=[]
    friend=[]
    a=[]
    for i in range(0,l):
          if  (q[i][0] not in a) and (q[i][1] not in a):
             friend.append(q[i])
             a.extend(q[i])
          elif  (q[i][0] not in a) and (q[i][1] in a):
               for k in range(0,len(friend)):
                   for w in range (0,len(friend[k])):
                     if friend[k][w]==q[i][1]:
                       s =k
                       break
                  
               friend[s].append(q[i][0])
               a.extend(q[i])
          elif  (q[i][1] not in a) and (q[i][0] in a):
             for k in range(0,len(friend)):
                   for w in range (0,len(friend[k])):
                     if friend[k][w]==q[i][0]:
                       s =k
                       break
             friend[s].append(q[i][1])
             a.extend(q[i])
          else:
               for k in range(0,len(friend)):
                  for w in range (0,len(friend[k])):
                     if friend[k][w]==q[i][0]:
                       s =k
                       p=1
                       break
               
               for m in range(0,len(friend)):
                  for w in range (0,len(friend[m])):
                    if friend[m][w]==q[i][1]:
                       h =m
                       p=1
                       break
               z=friend[h]
               if(friend[s]!=friend[h]):
                 friend[s].extend(friend[h])
                 del(friend[h])
               
          print (friend)
          for j in friend:
              
              c.append(len(j))
          print (max(c))
          ma= max(c)
          del(c)
          c=[]

q = int(input())
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
maxCircle(queries)
