#Same Direction Pointer
arr=[1,0,3,0,5,6,7,0]
i=0
for j in range(len(arr)):
    if arr[j] != 0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
print(arr)

#opposite direction
arr=[1,2,3,4,5]
i=0
j=len(arr)-1
while i < j:
    arr[i],arr[j]=arr[j],arr[i]

    i+=1
    j-=1
print(arr)

#Remove Duplicates from Sorted Array
arr=[1,1,2,3,3,4,4,5]
i=0
for j in range(1,len(arr)):
    if arr[j]!=arr[i]:
        i+=1
        arr[i]=arr[j]
print(arr[:i+1])