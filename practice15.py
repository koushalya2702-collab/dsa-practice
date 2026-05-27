#Average of Every Window

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
window_sum=sum(arr[:k])
averages=[]

averages.append(window_sum/k)
for i in range(k, len(arr)):
    window_sum-=arr[i-k]
    window_sum+=arr[i]
    averages.append(window_sum/k)
print(averages)

#First Negative Number in Every Window