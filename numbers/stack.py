n=[3,1,4,2,5,1]
res=[]
count=0
for x in n:
    while res and x > res[-1]:
        res.pop()
        count += 1
    res.append(x)
print(count)
        