#two pointers
arr=[1,2,3,4,5]
left=0
right=len(arr)-1
while left < right:
    arr[left],arr[right]=arr[right],arr[left]

    left+=1
    right-=1
print(arr)

#Rotate an Array
arr=[1,2,3,4,5]
k=2
k=k%len(arr)
arr=arr[-k:]+arr[:-k]
print(arr)


#Example
arr=[1,2,5,6,7,8,9]
k=8
k=k%len(arr)
arr=arr[-k:]+arr[:-k]
print(arr)
