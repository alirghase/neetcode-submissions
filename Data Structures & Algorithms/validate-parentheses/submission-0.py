class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            # if character is a closing bracket 
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if top_element != bracket_map[char]:
                    return False

            # if character is an opening bracket
            else:
                stack.append(char)
        return len(stack) == 0