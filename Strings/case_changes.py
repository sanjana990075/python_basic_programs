s="AbCs"
count=0
for i in range(len(s)-1):
    if  s[i].islower() and s[i+1].isupper():
        count+=1
    if s[i].isupper() and s[i+1].islower():
        count+=1
print(count)