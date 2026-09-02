#longest substring without repeating character
s="abcdeab"
seen=set()
left=0
max_length=0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[right])
    length=right-left+1
    max_length=max(length,max_length)
print(max_length)