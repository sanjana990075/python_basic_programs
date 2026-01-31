s=input()

result=[]
temp=s[0]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        temp+=s[i]
    else:
        result.append(temp)
        temp=s[i]
result.append(temp)
print("-".join(result))