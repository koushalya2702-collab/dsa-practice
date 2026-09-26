#find all the anagram in a string
s = "cbaebabacd"
p = "abc"
if len(p) > len(s):
    print([])
count1={}
count2={}
result=[]
for char in p:
    count1[char]=count1.get(char,0)+1
for char in s[:len(p)]:
    count2[char]=count2.get(char,0)+1
if count1==count2:
    result.append(0)
left=0
for right in range(len(p),len(s)):
    count2[s[right]]=count2.get(s[right],0)+1
    count2[s[left]]-=1
    if count2[s[left]]==0:
        del count2[s[left]]
    left+=1
    if count1==count2:
        result.append(left)

print(result)
