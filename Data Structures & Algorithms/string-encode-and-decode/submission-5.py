class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            slen = str(len(s))
            res += slen + "!" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        size = ""
        temp = ""
        length = len(s)
        strend = True
        for i in range(length):
            char = s[i]
            if char == "!" and strend:
                size = int(size)
                strend = False
                if size == 0:
                    res.append(temp)
                    strend = True
                    size = ""
            elif strend:
                size += char
            else:
                temp += char
                size -= 1
                if size < 1:
                    res.append(temp)
                    temp = ""
                    strend = True
                    size = ""
        
        return res

        