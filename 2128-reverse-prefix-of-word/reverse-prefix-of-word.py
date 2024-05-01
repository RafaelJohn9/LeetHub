class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word

        part_to_be_reversed =  list(word[:index + 1])
        part_to_be_reversed.reverse()
        other_part = word[index + 1:]
        reversed_part = "".join(part_to_be_reversed)
        new_word = reversed_part + other_part

        return new_word
