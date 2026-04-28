
#find second largest element

def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

#rotate array by k steps
def rotate(arr, k):
    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr

#remove element
def remove_element(arr, val):
    i = 0
    for j in range(len(arr)):
        if arr[j] != val:
            arr[i] = arr[j]
            i += 1
    return i