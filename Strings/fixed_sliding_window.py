"""
input1:a string s representing the chapter tittle
input2=length of the substring
output=return an integer representing the count of unique substring of a specific length
s=abcabc
k=3
output=3

abcabc= abc,bca,cab,abc,cab

"""

s="abcabc"
k=3
res=set()
for i in range(0,len(s)-k+1):
    res.add(s[i]+s[i+1]+s[i+2])

    
print(len(res))
        
    




