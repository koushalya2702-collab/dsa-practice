#Remove Duplicates from Sorted Array(same direction)
arr=[1,1,2,2,3]
i=0
for j in range(1,len(arr)):
    if arr[j]!=arr[i]:
        i+=1
        arr[i]=arr[j]
print(i+1)
print(arr[:i+1])


#Move Zeroes
arr = [0,1,0,3,12]
i=0
for j in range(len(arr)):
    if arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
print(arr)

#Remove Element
arr=[3,2,2,3]
val=3
i=0
for j in range(len(arr)):
    if arr[j]!=val:
        arr[i]=arr[j]
        i+=1
print(i)
print(arr[:i])