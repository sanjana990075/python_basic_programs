s="aaabbccbbc"
temp=s[0]
res=[]
k=3
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        temp+=s[i]
    else:
        res.append(temp)
        temp=s[i]
        
print(res)