class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l <= 1: return s
        minStart, maxLen, i = 0, 1, 0
        while i < l:
            if l - i <= maxLen / 2: break
            j, k = i, i
            while k < l - 1 and s[k] == s[k + 1]: k += 1
            i = k + 1
            while k < l - 1 and j and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1
            if k - j + 1 > maxLen: minStart, maxLen = j, k - j + 1
        return s[minStart: minStart + maxLen]
