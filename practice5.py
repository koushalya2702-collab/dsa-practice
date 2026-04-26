#array patern

#Find maximum element
arr=[1,2,3,5,7]
def find_max(arr):
    max_value=arr[0]
    for i in arr:
        if i > max_value:           #output:7
            max_value=i
    return max_value
print(find_max(arr))

#find minimum element
arr=[10,2,5,67,8]
def find_min(arr):
    min_value=arr[0]
    for i in arr:                   #output:2
        if i < min_value:
            min_value=i
    return min_value
print(find_min(arr))

#Find second largest element
array=[90,78,65,32]
def sec_large(arr):
    largest=arr[0]                  #output:78
    second=float('-inf')
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
        elif arr[i]>second and arr[i]!=largest:
            second=arr[i]
    return second
print(sec_large(array))

#Reverse array
arr=[1,2,3,4,5]
def rev_arr(arr):
    n=len(arr)
    new_arr=[]
    for i in range(n-1,-1,-1):          #output:    [5, 4, 3, 2, 1]
        new_arr.append(arr[i])
    return new_arr

print(rev_arr(arr))

#check array sorted or not
arr=[1,2,4,5,3]
def check_arr(arr):             #output:False
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
print(check_arr(arr))

#Remove duplicates
arr=[1,1,1,2,2,3,4,5,6]
def remove_duplicate(arr):
    n=len(arr)
    new_arr=[]                    #output:  [1, 2, 3, 4, 5]
    for i in range(n-1):
        if arr[i] not in new_arr:
            new_arr.append(arr[i])
    return new_arr
print(remove_duplicate(arr))

#Move zeros to end
arr=[1,0,3,0,35,0,5]
def move_zero(arr):
    new_arr=[]
    n=len(arr)
    for i in range(n-1):
        if arr[i]!=0:
            new_arr.append(arr[i])
    zero_count=len(arr)-len(new_arr)           #output: [1, 3, 35, 0, 0, 0, 0]
    for i in range(zero_count):
        new_arr.append(0)
    return new_arr
print(move_zero(arr))


#Rotate array
arr=[2,4,5,6,7]
def rotate_arr(arr):
    n=len(arr)
    new_arr=[]
    new_arr.append(arr[n-1])                #output:[7, 2, 4, 5, 6]
    for i in range(n-1):
        new_arr.append(arr[i])
    return new_arr
print(rotate_arr(arr))
