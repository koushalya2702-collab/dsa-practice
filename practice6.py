#Hashmap
#Two sum
arr=[1,2,3,4,5]
target=9
def two_sum(arr,target):
    d={}
    for i,num in enumerate(arr):
        if target-num in d:
            return [d[target-num],i]
        d[num]=i
print(two_sum(arr,target))


#Frequency count
arr=[1,1,1,2,2,3,3,4,5,6]
def frequency_count(arr):
    d={}
    for num in arr:
        if num in d:
            d[num]+=1
        else:
            d[num]=1
    return d
print(frequency_count(arr))

#First unique element
arr=[1,1,3,3,4,5]
def unique_element(arr):
    d={}
    for num in arr:
        d[num]=d.get(num,0)+1
    for num in arr:
        if d[num]==1:
            return num
print(unique_element(arr))

#valid anagram
a="listen"
b="silent"
def is_anagram(a,b):
    if len(a)!=len(b):
        return False
    d={}
    for char in a:
       d[char]=d.get(chr,0)+1
    for char in b:
        if char not in d:
            return False
        d[char]-=1
        if d[char]==0:
            del d[char]
    return len(d)==0
print(is_anagram(a,b))
            

#
arr=[1,1,2,2,3,4]
def frequency_count(arr):
    d={}
    for num in arr:
        d[num]=d.get(num,0)+1
    return d
print(frequency_count(arr))


