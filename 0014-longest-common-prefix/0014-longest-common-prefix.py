class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if the list has only one string we return the  string
        if len(strs) == 1:
            return strs[0]

        # Create a variable to hold the suggested prefix
        common_prefix = ""

        # Compare the first two strings
        first_str = strs[0]
        second_str = strs[1]
        shortest_str_length = min(len(first_str), len(second_str))

        for i in range(shortest_str_length):
            if first_str[i]  == second_str[i]:
                common_prefix += first_str[i]
            else:
                break
        
        # if array contains only two elements we return prefix
        if len(strs) == 2:
            return common_prefix
        
        for i in range(2, len(strs)):
            string = strs[i]
            len_string = len(string)

            for i in range(len(common_prefix)):
                if len_string <= i:
                    common_prefix = common_prefix[:i]
                    break

                if string[i]  == common_prefix[i]:
                    continue
                else:
                    common_prefix = common_prefix[:i]
                    break
                
        
        return common_prefix


