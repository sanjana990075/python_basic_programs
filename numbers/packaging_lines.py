s="1a2b3c4d5"
count=0
for i in range(1,len(s)-1):
    if s[i].isalpha():
        if s[i-1].isdigit() and s[i+1].isdigit():
            count+=1
print(count)