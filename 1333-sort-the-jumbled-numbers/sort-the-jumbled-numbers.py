class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_values: Set[int] = set()
        mapped_num: Dict[int, List[int]] = {}

        for num in nums:
            digit_map = ""
            for digit in str(num):
                digit_map += str(mapping[int(digit)])
            
            list_map = mapped_num.get(int(digit_map), [])
            list_map.append(num)
            mapped_num[int(digit_map)] = list_map
            mapped_values.add(int(digit_map))
        
        mapped_values = sorted(mapped_values)

        result = []
        for mapped in mapped_values:
            for val in mapped_num[mapped]:
                result.append(val)
        
        return result