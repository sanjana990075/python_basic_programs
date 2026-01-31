n="NNYNNN"
k=3
n_count=0
count=0
for i in range(len(n)):
    if n[i]=='N':
        n_count+=1
    else:
        if n_count>=k:
            count+=1
        n_count=0
if n_count>=2:
    count+=1
print(count)
    
    