class Solution:
    def partition(self, s: str):
        res = []
        part = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start):

            if start == len(s):
                res.append(part.copy())
                return

            for end in range(start, len(s)):

                if isPalindrome(start, end):

                    part.append(s[start:end+1])

                    dfs(end + 1)

                    part.pop()

        dfs(0)

        return res
        