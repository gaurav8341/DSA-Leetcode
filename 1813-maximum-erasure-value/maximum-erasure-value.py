class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # delete sub array
        # all elems in sub array should be unique
        # get max score, wcore is addition on all elem in  subarray

        # sliding window of variable size
        # if we find any elem which is repeated 
        # then new lower boiund of sub array is elem_idx which is repeated + 1 

        # lets do simple approach first
        subarray = dict()
        count, max_count = 0, 0
        l, r = 0, 0 # r would be non incusive
        for i, c in enumerate(nums):
            # check if c is in subarray
            if c in subarray:
                # c is in subarray
                # we take old idx
                new_l = subarray[c] + 1
                while l < new_l:
                    count -= nums[l]
                    subarray.pop(nums[l], None)
                    l += 1
                # now we have new l 
                
            # else:
            subarray[c] = i
            count += c
                # r += 1
            max_count = max(count, max_count)
        
        return max_count