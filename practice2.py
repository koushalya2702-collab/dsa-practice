#reverse an array

# arr=[1,2,3,4]
# left=0
# right=len(arr)-1
# while left<right:
#    arr[left],arr[right]=arr[right],arr[left]
#    left+=1
#    right-=1
# print(arr)

# #check palindrome
# arr=[1,2,2,1]
# left=0
# right=len(arr)-1
# is_palindrome=True
# while left<right:
#    if arr[left]!=arr[right]:
#       is_palindrome=False
#       break
#    left+=1
#    right-=1
# print(is_palindrome)
      
#count pair sum
arr=[1,2,3,4]
target=5
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(arr[i],arr[j])
            count+=1
print("Total pairs:",count)
