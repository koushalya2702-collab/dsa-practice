#Finding Maximum
arr=[34,67,54,99]
max=arr[0]
for num in arr:
    if num > max:
        max=num
print(max)

#Finding Minimum
arr=[1,45,67,0]
min=arr[0]
for num in arr:
    if num < min:
        min=num
print(min)

#Counting Frequency
arr=[1,1,2,3,3,2,4,5,4,4,6]
freq={}
for num in arr:
    if num in freq:
        freq[num] +=1
    else:
        freq[num]=1
print(freq)


#Shorter Frequency Pattern
arr=[1,2,3,4,4,4,3,2]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
print(freq)