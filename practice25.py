#sliding window(maximum avg subarray)

nums=[1,12,-5,-6,50,3]
k=4
window_sum=sum(nums[:k])
max_sum=window_sum
left = 0
for right in range(k,len(nums)):
    window_sum+=nums[right]
    window_sum-=nums[left]
    left += 1
    max_sum=max(window_sum,max_sum)
print(max_sum/k)