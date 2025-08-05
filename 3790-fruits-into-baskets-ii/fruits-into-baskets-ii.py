class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        count = 0
        for i in range(n):
            for j in range(n):
                # print(fruits, baskets, i, j)
                if fruits[i] <= baskets[j]:
                    count += 1
                    baskets[j] = 0
                    break
        
        return n - count