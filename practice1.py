# #find largest element

# def largest_element(arr):
#     largest_element=arr[0]
#     for i in range(len(arr)):
#         if a[i]>largest_element:
#             largest_element=arr[i]
#     return largest_element
# a=[8,9,5,4,61]
# print(largest_element(a))


# #loop through array(pattern)
# arr=[3,4,6,7,8]
# for i in range(len(arr)):
#     print(arr[i])

# #find sum of array
# arr=[4,6,2,3]
# total=0
# for num in arr:
#     total+=num
# print(total)

# #find maximum element
# arr=[6,7,3,91,19]
# max_element=arr[0]
# for num in arr:
#     if num > max_element:
#         max_element=num
# print(max_element)

# #find the minimum element
# arr=[2,5,8,92,1]
# min_element=a[0]
# for num in arr:
#     if num < min_element:
#         min_element=num
# print(min_element)

#count even numbers
arr=[2,1,3,7,8]
count=0
for num in arr:
    if num%2==0:
        count+=1
print(count)


#numbers greter tahn 5
arr=[4,7,8,9,5,9]
count=0
for num in arr:
    if num > 5:
        count+=1
print(count)
