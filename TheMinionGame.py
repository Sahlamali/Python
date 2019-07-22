#Kevin and Stuart want to play the 'The Minion Game'.
#Game Rules
#Both players are given the same string, .
#Both players have to make substrings using the letters of the string .
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels. 
#The game ends when both players have made all possible substrings. 

#Scoring
#A player gets +1 point for each occurrence of the substring in the string .

#Input Format
#A single line of input containing the string . 
#Note: The string  will contain only uppercase letters: .

#Output Format
#Print one line: the name of the winner and their score separated by a space.
#If the game is a draw, print Draw.

#Sample Input
#BANANA

#Sample Output
#Stuart 12


#The Program starts here
def minion_game(stri):
    b=[]
    c=[]
    string=stri.lower()
    n=len(string)
    
    for i in string:
        if ((i=='a')or(i=='e')or(i=='o')or(i=='i')or(i=='u')):
            b.extend(i)
        else:
            c.extend(i)
    Stuart_c = int(len(c))
    Kevin_c = int(len(b))
    #Making words for Stuart
    j=0
    if(Stuart_c>0):
        for i in range(0,n+1):
            if(c[j]==string[i]):
                e=int(len(string[i+1:]))
                Stuart_c=int(Stuart_c)+int(e)
                j=j+1
               # print (j)
            if(j==len(c)):
                break
    if(Kevin_c>0):
    #Making words for Kevin
     j=0
     for i in range(0,n+1):
            if(b[j]==string[i]):
                e=int(len(string[i+1:]))
                Kevin_c=int(Kevin_c)+int(e)
                j=j+1
               # print (j)
            if(j==len(b)):
                break
            
    if(Stuart_c>Kevin_c):
        print("Stuart ",end="")
        print(Stuart_c)
    elif(Stuart_c<Kevin_c):
        print("Kevin ",end="")
        print(Kevin_c)
    else:
        print("Draw")   
if __name__ == '__main__':
    s = input()
    minion_game(s)
