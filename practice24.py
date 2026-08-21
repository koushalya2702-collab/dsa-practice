#Remove Duplicates from Sorted Array
arr=[0,0,1,1,1,2,2,3,3,4]
i=0
for j in range(1,len(arr)):
    if arr[i] != arr[j]:
        i += 1
        arr[i]=arr[j]
print(arr[:i+1])


#remove zeros at the end
arr=[0,5,0,8,7,6,0,7,0]
left=0
for right in range(len(arr)):
    if arr[right] != 0:
        arr[left],arr[right]=arr[right],arr[left]
        left += 1
print(arr)


#remove element
arr=[2,3,4,4,5,4]
val=4
left=0
for right in range(len(arr)):
    if arr[right]!=val:
        arr[left]=arr[right]
        left+=1
print(arr)
