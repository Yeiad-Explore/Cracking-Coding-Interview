def two_sum(nums, target):
    store = {}
    for i, num in enumerate(nums):
        c = target - num
        if c in store:
            return [store[c], i]
        store[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9)) # Output: [0, 1]
print(two_sum([3, 2, 4], 6)) # Output: [1, 2]
print(two_sum([3, 3], 6)) # Output: [0, 1]

# Time Complexity:O(1)

# Space Complexity: O(n)