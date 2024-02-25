class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        
        for i, char in enumerate(s):
            if char not in stack:
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    stack.pop()
                stack.append(char)
        return ''.join(stack)