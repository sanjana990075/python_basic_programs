"""
either add a 3 kilograms
or multiply with 2
y=1
{3,0}=2
y=2
{6,0,3}

y=3
{}
"""

curr={0}
y=2
for _ in range(y):
    next=set()
    for w in curr:
        next.add(w+3)
        next.add(w*2)
    curr=next
print(len(curr))