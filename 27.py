#minimum size subarry sum
nums=[2,3,1,2,4,3]
target=7
left=0
minimum_length=float('inf')
window_sum=0
for right in range(len(nums)):
    window_sum+=nums[right]
    while window_sum>=target:
        length=right-left+1
        minimum_length=min(length,minimum_length)
        window_sum-=nums[left]
        left+=1
    if minimum_length==float('inf'):
        print(0)
print(minimum_length)
