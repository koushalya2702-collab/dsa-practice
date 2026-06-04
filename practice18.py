
#set

s="hello"
seen=set()
for ch in s:
    if ch in seen:
        print("Duplicate:",ch)
    seen.add(ch)

print(seen)

#Hashmap

arr=[1,1,2,3,3,4,5,5]
freq={}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)


#Example
word="banana"
freq={}
for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch]=1
print(freq)