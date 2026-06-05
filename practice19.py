#SET PROBLEMS: Remove Duplicates

arr=[1,2,2,3,3,4]
result=set(arr)
print(result)

#Check Duplicate Exists
arr=[1,2,3,4,2]
seen=set()
duplicate=False
for num in arr:
    if num in seen:
        duplicate=True
        break
    seen.add(num)
print(duplicate)


#Count Distinct Elements

arr=[1,1,2,3,4,5,5,]
seen=set(arr)
print(len(seen))

#First Repeated Character
s="programming"
seen=set()

for ch in s:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)


