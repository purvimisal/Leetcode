class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        start = 0
        for end in range(0,len(s)):
            if s[end] in seen:
                start = max(start,seen[s[end]]+1)
            seen[s[end]] = end
            max_len = max(max_len,end-start+1)
        return max_len
