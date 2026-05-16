#Palindrome
s="madam"
left=0
right=len(s)-1
is_palindrome=True
while left < right:
    if s[left]!=s[right]:
        is_palindrome=False
    left+=1
    right-=1
print(is_palindrome)

#Pair Sum in Sorted Array
arr=[4,5,6,7,8]
target=13
left=0
right=len(arr)-1
while left < right:
    total=arr[left]+arr[right]
    if total==13:
        print(left,right)
        break
    elif total < 13:
        left+=1
    else:
        right-=1
    
#move zeros
arr=[9,0,4,0,6,0,7,8]
slow=0
for fast in range(len(arr)):
    if arr[fast]!=0:
       arr[slow],arr[fast]=arr[fast],arr[slow]
       slow+=1
print(arr) 
