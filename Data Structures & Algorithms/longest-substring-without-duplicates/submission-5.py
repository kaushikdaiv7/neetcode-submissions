class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        if n == 0:
            return 0

        left, right = 0, 0
        seen_chars = set()
        max_len = 1

        while right < n:
            if s[right] not in seen_chars:
                seen_chars.add(s[right])
            else:
                max_len = max(max_len, right - left)
                while s[left] != s[right]:
                    seen_chars.remove(s[left])
                    left+= 1
                left += 1
            right += 1
        
        print(left, right)
        return max(max_len, right - left)