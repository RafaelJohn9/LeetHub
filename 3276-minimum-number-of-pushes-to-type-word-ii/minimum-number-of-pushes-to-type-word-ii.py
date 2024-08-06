from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Finds the minimum pushes to enter a word in a phone's keypad
        """
        CONST_KEYS = '1*#0'
        NUM_OF_KEYS = 8
        KEYPAD = {}

        # Step 1: Sort word by frequency in descending order
        count = Counter(word)
        sorted_word = ''.join(sorted(word, key=lambda x: count[x], reverse=True))

        # Helper function to check if a character is a special character
        def is_special(char: str) -> bool:
            return char in CONST_KEYS

        min_pushes = 0
        uniq_index = 0

        for char in sorted_word:
            if char in KEYPAD:
                min_pushes += KEYPAD[char]
                continue

            # Assign the number of pushes based on the unique index and special character check
            if is_special(char) or uniq_index < NUM_OF_KEYS:
                KEYPAD[char] = 1
            else:
                KEYPAD[char] = (uniq_index // NUM_OF_KEYS) + 1

            min_pushes += KEYPAD[char]
            uniq_index += 1

        return min_pushes
