#longest repeating character replacement
s = "ABAB"
k = 2
left=0
count={}
max_length=0
for right in range(len(s)):
    count[s[right]]=count.get(s[right],0)+1
    max_count=max(count.values())
    while (right-left+1)-max_count > k:
        count[s[left]]-=1
        left+=1
        max_count=max(count.values())
    length=right-left+1
    max_length=max(max_length,length)
print(max_length)

