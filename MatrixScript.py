#The given matrix script is a N X M grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&). If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

#Input Format
#The first line contains space-separated integers  N(rows) and M (columns) respectively. 
#The next N lines contain the row elements of the matrix script.

#Output Format
Print the decoded matrix script.

#Sample Input 0

#7 3
#Tsi
#h%x
#i #
#sM 
#$a 
##t%
#ir!

#Sample Output 0

#This is Matrix#  %!


#Program

import re
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
strin =""
b=[]
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
flag=[]
for j in range(0,m):
    for i in matrix:
        strin=strin+(i[j])

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", strin))
