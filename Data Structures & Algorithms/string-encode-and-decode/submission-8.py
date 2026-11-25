class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = str(len(s)) + ";"
            res = res + l + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 1
        while l < len(s):
            l, r = 0, 1
            length = s[l]

            while s[r]!= ";":
                length += s[r]
                r += 1

            r += 1
            length = int(length)
            res.append(s[r: r + length])
            if r + length < len(s):
                s = s[r + length:]
            else:
                break

        return res