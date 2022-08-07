class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Flipping Horizontally
        for k in range(len(image)):
            i, j = 0, len(image[k]) - 1
            while i < j:
                image[k][i], image[k][j] = image[k][j], image[k][i]
                i += 1
                j -= 1
        # Inverting
        for k in range(len(image)):
            for i in range(len(image[k])):
                if image[k][i]:
                    image[k][i] = 0
                else:
                    image[k][i] = 1
        return image