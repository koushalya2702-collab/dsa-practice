# #HASHMAP PROBLEMS: Frequency of Numbers

# arr = [1,1,2,2,2,3]

# freq = {}

# for num in arr:

#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# print(freq)

# #Frequency of Characters

# word = "banana"

# freq = {}

# for ch in word:

#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print(freq)

# # #First Non-Repeating Character

# s="aabbcde"
# freq={}
# for ch in s:
#     freq[ch]=freq.get(ch,0)+1
# for ch in s:
#     if freq[ch]==1:
#         print(ch)
#         break


#Highest Frequency Element

arr=[1,1,1,2,2,3]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
answer=max(freq,key=freq.get)
print(answer)


#
arr = [1,1,1,2,2,3]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

answer = max(freq, key=freq.get)

print(answer)