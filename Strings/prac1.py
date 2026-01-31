s="aabbcccc"
res=[]
temp=s[0]
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        temp+=s[i]
    else:
        res.append(temp)
        temp=s[i]
res.append(temp)
print('-'.join(w for w in res))