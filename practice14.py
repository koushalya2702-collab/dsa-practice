#Sliding Window Problems
arr=[2,1,5,1,3,2]
k=3

window_sum=sum(arr[:k])
max_sum=window_sum

for i in range(k,len(arr)):
    window_sum -= arr[i-k]

    window_sum +=arr[i]

    max_sum=max(max_sum,window_sum)
print(max_sum)

#Find the maximum sum of subarray of size 4
arr = [4, 2, 1, 7, 8, 1, 2, 8]
k = 4
window_sum=sum(arr[:k])
max_sum=window_sum

for i in range(k,len(arr)):
    window_sum -= arr[i-k]

    window_sum += arr[i]

    max_sum=max(window_sum,max_sum)
print(max_sum)

#Maximum Average
arr = [5, 3, 8, 2, 6, 1, 4]

k = 3
window_sum=sum(arr[:k])
max_avg=window_sum/k

for i in range(k,len(arr)):
    window_sum -= arr[i-k]
    window_sum += arr[i]

    avg=window_sum/k
    max_avg=max(max_avg,avg)
print(max_avg)

#Find the minimum sum of subarray of size 2
arr = [7, 2, 5, 1, 6, 3]
k = 2

window_sum=sum(arr[:k])
min_sum=window_sum

for i in range(k,len(arr)):
    window_sum -= arr[i-k]
    window_sum += arr[i]

    min_sum=min(min_sum,window_sum)
print(min_sum)
