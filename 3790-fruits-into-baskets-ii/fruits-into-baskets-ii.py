class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        count = 0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                # print(fruits, baskets, i, j)
                if fruits[i] <= baskets[j]:
                    count += 1
                    baskets[j] = 0
                    break
        
        print(count)
        return len(fruits) - count