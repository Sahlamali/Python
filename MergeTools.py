#Consider the following:

#A string,s, of length n.
#An integer, k, where k is a factor of n.
#We can split s into  n/k subsegments where each subsegment,ti , consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

#The characters in ui are a subsequence of the characters in ti .
#Any repeat occurrence of a character is removed from the string such that each character in ui  occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti , then do not include the character in string ui .
#Given  and , print  lines where each line  denotes string .

#Input Format
#The first line contains a single string denoting s. 
#The second line contains an integer,k , denoting the length of each subsegment.

#Output Format
#Print  n/k lines where each line i  contains string ui .

#Program Starts here
def merge_the_tools(string, k):
    # your code goes here
    n= len(string)//k
    l=[]
    
    j=0
    for i in range(0,n):
       s=[]
       l.append(string[j:k+j])
       s.extend(string[j:k+j])
       li=list(dict.fromkeys(s))
       del(s)
       st="".join(li)
       print(st)
       j=j+k 
    #print(l)

string, k = input(), int(input())
merge_the_tools(string, k)
