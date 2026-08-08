class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(word)
            res.append('#')

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        word = ""
        res = []
        for ch in s:
            if ch == '#':
                res.append(word)
                word = ""
            else:
                word += ch

        return res

sol = Solution()
enc = sol.encode(["w213e"])
dec = sol.decode(enc)
print(f"The encoded verision is : {enc}")
print(f"The decoded verision is : {dec}")

