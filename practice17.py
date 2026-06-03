#Maximum Consecutive Ones After Flipping K Zeros

arr = [1,1,1,0,0,0,1,1,1,1,0]

k = 2

left=0
zero_count=0
max_length=0

for right in range(len(arr)):
    if arr[right]==0:
        zero_count += 1

    while zero_count > k:
        if arr[left]==0:
            zero_count-=1
        left += 1
    max_length=max(max_length,right-left+1)
print(max_length)


