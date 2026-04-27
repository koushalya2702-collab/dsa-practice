#check duplicates
arr=[1,1,2,2,4,5,6]
def contain_duplicates(arr):
    s=set()
    for num in arr:
        if num in s:
           return True
        else:
            s.add(num)
    return False
print(contain_duplicates(arr))


#intersection of two array
a=[1,2,3,4]
b=[2,3,5,6]
def intersection(a,b):
    s=set(a)
    result=[]
    for num in b:
        if num in s:
            result.append(num)
    return result
print(intersection(a,b))



