nums = [1,2,3,4]
ans = []

for i in range(len(nums)):
    prod = 1
    for j in range(len(nums)):
        if i != j:
            prod *= nums[j]
    ans.append(prod)

print(ans)