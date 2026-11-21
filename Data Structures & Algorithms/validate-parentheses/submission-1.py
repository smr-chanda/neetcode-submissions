class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 :
            return False
        stack = []
        hashes_rev = {"}": "{", "]": "[", ")": "("}
        try:
            for i in s:
                if i in hashes_rev:
                    latest_element = stack.pop()
                    if hashes_rev[i] != latest_element:
                        return False
                else:
                    stack.append(i)
            
            if stack == []:
                return True
            else:
                return False
        except Exception:
            return False