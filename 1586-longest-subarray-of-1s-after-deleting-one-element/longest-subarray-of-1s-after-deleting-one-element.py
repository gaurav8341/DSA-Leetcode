class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # idea is parse the list

        l = 0
        idx_0 = l if nums[l] == 0 else -1 
        _max = 0
        for r in range(1, len(nums)):
            # while nums[l] == 0:
            # print(r, l, idx_0)
            if nums[r] == 0:
                # check if prev 0 exists if not do nothing 
                # if it does then reset l
                if idx_0 >= 0:
                    l = idx_0 + 1
                idx_0 = r
            _max = max(_max, r - l) # as we are removing an elem 
        return _max
