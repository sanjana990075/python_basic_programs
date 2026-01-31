"""input 1 : an integer value n representing the number of rows in grid g
    input2: an integer value m representing the number of cols in g
    input 3 : a string s
    output : spiral matrix string 
"""

n=int(input())
m=int(input())
s=input()
grid=[]
i=0
for r in range(n):
    row=[]
    for c in range(m):
        if i <len(s):
            row.append(s[i])
            i+=1
        else:
            row.append(' ')
    grid.append(row)
print(grid)

res=""

while grid:
    if grid:
        res+="".join(grid.pop(0))
    if grid:
        res+="".join([row.pop() for row in grid])
    if grid:
        res+="".join(grid.pop()[::-1])
    if grid:
        res+="".join([row.pop(0) for row in grid][::-1])
print(res)
    
