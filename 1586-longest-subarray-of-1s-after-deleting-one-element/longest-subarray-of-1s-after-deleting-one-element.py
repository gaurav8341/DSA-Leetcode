class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # idea is parse the list

        # l = 0
        # idx_0 = l if nums[l] == 0 else -1 
        # _max = 0
        # for r in range(1, len(nums)):
        #     # print(r, l, idx_0)
        #     if nums[r] == 0:
        #         # check if prev 0 exists if not do nothing 
        #         # if it does then reset l
        #         if idx_0 >= 0:
        #             l = idx_0 + 1
        #         idx_0 = r
        #     _max = max(_max, r - l) # as we are removing an elem we are not adding +1 
        # return _max

        # class Solution:
    # def longestSubarray(self, nums: List[int]) -> int:
        left, zeros, res = 0, 0, 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            res = max(res, right - left)
        
        return res
