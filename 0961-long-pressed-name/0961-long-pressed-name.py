class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_index = typed_index = 0

        while typed_index < len(typed):
            if name_index < len(name) and name[name_index] == typed[typed_index]:
                name_index += 1
                typed_index += 1
            elif typed_index > 0 and typed[typed_index] == typed[typed_index - 1]:
                typed_index += 1  # Allow repeated characters in "typed"
            else:
                return False  # Mismatch found
        
        return name_index == len(name)  # Ensure all characters in "name" were matched
