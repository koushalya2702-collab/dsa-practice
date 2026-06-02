#Sliding window average size

arr=[2,3,1,2,4,3]
left=0
window_sum=0
min_len=float('inf')
for right in range(len(arr)):
    window_sum += arr[right]
    while window_sum >= 7:
        min_len=min(min_len,right-left+1)
        window_sum -= arr[left]
        left += 1
print(min_len)

#Longest Subarray Problem

arr = [1, 2, 1, 0, 1, 1, 0]
left=0
window_sum=0
max_len=0
for right in range(len(arr)):
    window_sum += arr[right]
    while window_sum >= 4:
        max_len=max(max_len,right-left+1)
        window_sum -= arr[left]
        left += 1
print(max_len)


