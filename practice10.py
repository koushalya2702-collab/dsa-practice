#Trapping Rain Water


def trap(height):
    l, r = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    
    while l < r:
        if height[l] < height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                water += left_max - height[l]
            l += 1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                water += right_max - height[r]
            r -= 1
    
    return water


#First Missing Positive


def first_missing_positive(nums):
    n = len(nums)
    
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1


#Maximum Product Subarray


def max_product(nums):
    max_p = min_p = ans = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_p, min_p = min_p, max_p
        
        max_p = max(nums[i], max_p * nums[i])
        min_p = min(nums[i], min_p * nums[i])
        
        ans = max(ans, max_p)
    
    return ans


#Sliding Window Maximum

from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    res = []
    
    for i in range(len(nums)):
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            res.append(nums[dq[0]])
    
    return res


#Minimum Window Substring


def min_window(s, t):
    from collections import Counter
    
    need = Counter(t)
    missing = len(t)
    l = start = end = 0
    
    for r, ch in enumerate(s, 1):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        
        if missing == 0:
            while l < r and need[s[l]] < 0:
                need[s[l]] += 1
                l += 1
            
            if end == 0 or r - l < end - start:
                start, end = l, r
            
            need[s[l]] += 1
            missing += 1
            l += 1
    
    return s[start:end]