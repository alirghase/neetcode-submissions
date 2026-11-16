class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {')': '(', '}': '{', ']':'['}
        stack = []

        for char in s:
            if char in close_open:
                if not stack or stack[-1] != close_open[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0