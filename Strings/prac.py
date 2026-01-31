s=123456
k=3
res=[]
for i in range(len(str(s))-k+1):
    res.append(s[i:i+k])
print(res)
    