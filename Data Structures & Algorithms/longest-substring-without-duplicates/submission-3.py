class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        r =0
        tracker = {}
        ans = 0
        while r<(len(s)):
            if s[r] in tracker:
                l =max(tracker[s[r]]+1, l)
            tracker[s[r]] = r
            ans = max(ans,(r-l+1))
            r+=1
        return ans