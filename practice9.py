#Best Time to Buy and Sell Stock


def max_profit(prices):
    min_price = float('inf')
    profit = 0
    
    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    
    return profit

#Container With Most Water


def max_area(height):
    l, r = 0, len(height) - 1
    ans = 0
    
    while l < r:
        h = min(height[l], height[r])
        ans = max(ans, h * (r - l))
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return ans


#Product of Array Except Self

def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    
    return res

#Maximum Subarray (Kadane’s Algorithm)
def max_subarray(nums):
    curr = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        curr = max(nums[i], curr + nums[i])
        max_sum = max(max_sum, curr)
    
    return max_sum

#two sum unsorted array

def two_sum(nums, target):
    d = {}
    
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i