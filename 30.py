#permutation in string
s1 = "ab"
s2 = "eidbaooo"
if len(s1)>len(s2):
    print(False)
count1={}
count2={}
for char in s1:
    count1[char]=count1.get(char,0)+1
for char in s2[:len(s1)]:
    count2[char]=count2.get(char,0)+1
if count1==count2:
    print(True)
left=0
found=False
for right in range(len(s1),len(s2)):
    count2[s2[right]]=count2.get(s2[right],0)+1
    count2[s2[left]]-=1
    if count2[s2[left]]==0:
        del count2[s2[left]]
    left+=1
    if count1==count2:
        print(True)
        found=True
        break
if not found:
    print(False)

    

