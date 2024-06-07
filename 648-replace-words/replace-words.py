class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary_set = set(dictionary)
        split_sentence = sentence.split()
        
        def find_root(word):
            for i in range(1, len(word) + 1):
                if word[:i] in dictionary_set:
                    return word[:i]
            return word
        
        replaced_words = [find_root(word) for word in split_sentence]
        return ' '.join(replaced_words)
