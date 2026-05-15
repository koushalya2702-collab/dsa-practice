#traversing array
arr=[1,2,3,4]
for i in arr:
    print(i)


#find sum
arr=[4,6,7,8]
total=0
for i in arr:
    total+=i
print(total)

#find the largest element
arr=[5,7,8,9]
largest=arr[0]
for i in arr:
    if i > largest:
        largest=i
print(largest)

#count even numbers
arr=[3,5,6,8,4]
count=0
for i in arr:
    if i % 2==0:
        count+=1
print(count)

#Reverse Array
arr=[4,6,8,7]
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)

#Second Largest Element
arr=[5,3,7,9]
largest=arr[0]
second=float('-inf')
for i in range(1,len(arr)):
    if arr[i]>largest:
        second=largest
        largest=arr[i]
    elif arr[i]>second and arr[i]!=largest:
        second=arr[i]
print(second)


 #Frequency Count
arr = [1, 2, 2, 3, 1]

for i in arr:
    print(i, arr.count(i))   #after using hashmap

#check sorted_array
arr=[1,2,3,4,5]
sorted_array=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        sorted_array=False
print(sorted_array)

