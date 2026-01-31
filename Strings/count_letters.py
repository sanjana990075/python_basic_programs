s="sanjana"
res={}
for ch in s:
    if ch in res:
        res[ch]+=1
    else:
        res[ch]=1
print(res)

res1={}
for ch in s:
    res1[ch]=res1.get(ch,0)+1
print(res1)

from collections import Counter

fre1=Counter(s)
print(fre1)