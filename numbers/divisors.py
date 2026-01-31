a=[1,2,3,4]
x=3
b=[]
for i in range(len(a)):
    if i<len(a)-1:
        b.append(a[i]+a[i+1])
    if i==len(a)-1:
        b.append(a[i]+a[0])
print(b)
res=[]
for i in b:
    if i%3==0:
        res.append(i)
print(sum(res))