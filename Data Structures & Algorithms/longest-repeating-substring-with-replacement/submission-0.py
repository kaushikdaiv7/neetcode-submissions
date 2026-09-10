class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 1
        dict_ = defaultdict(int)
        l = 0

        for r in range(n):
            dict_[s[r]] += 1

            if (r - l + 1) - max(dict_.values()) > k:
                dict_[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

            



        