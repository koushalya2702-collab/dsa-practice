#sum problem using pointer
arr=[1,2,3,4]
target=5
left=0
right=len(arr)-1
while left< right:
    if arr[left]+arr[right] == target:
        print(arr[left],arr[right])
        left += 1
        right -= 1
    elif arr[left]+arr[right]<target:
        left += 1
    else:
        right -= 1


#Count Number of Swaps
def count_swaps(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return swaps

print(count_swaps([4, 3, 2, 1]))  


#Second Largest Element
def second_largest(arr):
    n = len(arr)

    for i in range(2):   # only 2 passes
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr[-2]


print(second_largest([7, 2, 9, 4]))  # Output: 7


#Move Zeros to End
def move_zeros(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] == 0 and arr[j+1] != 0:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]