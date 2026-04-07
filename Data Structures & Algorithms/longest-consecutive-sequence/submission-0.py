class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        longest = 0
        for num in n:
            if num - 1 not in n:
                curr = num
                length = 1
                while curr + 1 in n:
                    curr += 1
                    length += 1
                longest = max(longest, length)
        return longest
        