class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
         res = []
         i = 0
         n = len(s)

         while i < n:
            j = i                    

            while j < n and s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)

            i = j + 1 + length

         return res
