class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)

        dict_ = {'}': '{', ']': '[', ')': '('}

        for i in range(n):
            if s[i] in {'{', '[', '('}:
                stack.append(s[i])
            elif stack and stack[-1] == dict_[s[i]]:
                stack.pop()
            else:
                return False

        return True if not stack else False
        