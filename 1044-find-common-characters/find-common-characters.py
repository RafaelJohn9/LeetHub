from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        
        # Initialize the frequency counter with the first word's character counts
        common_freq = Counter(words[0])
        
        # Intersect the frequency counter with the character counts of each subsequent word
        for word in words[1:]:
            word_freq = Counter(word)
            # Perform intersection by taking minimum frequency for each character
            common_freq &= word_freq
        
        # Expand the character counts into the result list
        result = []
        for char, count in common_freq.items():
            result.extend([char] * count)
        
        return result