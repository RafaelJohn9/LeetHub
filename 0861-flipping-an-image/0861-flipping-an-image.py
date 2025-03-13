class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            # reverse the row
            image[i] = image[i][::-1]

            # invert them horizontally
            image[i] = [1 if num == 0 else 0 for num in image[i] ]
        
        return image