import heapq

class Solution:
    def minimumDifference(self, nums):
        n3 = len(nums)
        n = n3 // 3

        leftMin = [0] * n3
        rightMin = [0] * n3

        # Max heap for left part (invert numbers to simulate max-heap)
        maxHeap = []
        leftSum = 0
        for i in range(n3):
            heapq.heappush(maxHeap, -nums[i])
            leftSum += nums[i]
            if len(maxHeap) > n:
                leftSum += heapq.heappop(maxHeap)
            if i >= n - 1:
                leftMin[i] = leftSum

        # Min heap for right part
        minHeap = []
        rightSum = 0
        for i in range(n3 - 1, -1, -1):
            heapq.heappush(minHeap, nums[i])
            rightSum += nums[i]
            if len(minHeap) > n:
                rightSum -= heapq.heappop(minHeap)
            if i <= n3 - n:
                rightMin[i] = rightSum

        # Calculate minimum difference
        result = float('inf')
        print(leftMin, rightMin)
        for i in range(n - 1, n3 - n):
            result = min(result, leftMin[i] - rightMin[i + 1])

        return result


# class Solution:
    # def minimumDifference(self, nums: List[int]) -> int:
        # we can remove elements in any order 
        # but the first - second calc must happen taking the order into account.

        # we need least possible diff. 
        # min detected heap selected

        # un optimized soln would be 
        # go through all possibilities and take the min one.

        # minimize the diff betn sum of n smallest elem in lft third and sum of n largest elem in right third

        # if we remove largest elem from left and smallest elem from right 
        # this is solved. 
        # If we had gauurenty if nums len will be even then this was easy 
        # but that is not given. in midle half smallest elem will go to left and largest will go to right
        """
        n = len(nums) // 3
        maxheap = [] # this is for left partition
        leftMins = [0] * len(nums)
        rightMaxs = [0] * len(nums)

        leftsum = 0
        for i in range(n):
            heapq.heappush(maxheap, -nums[i])
            leftsum += nums[i]
        leftMins[n - 1] = leftsum

        for i in range(n , len(nums) - n):
            if nums[i] < -maxheap[0]:
                # only the smallest elem be taken in second n elems
                # here as we are taking the smaller number 
                # we are discarding largest number taken in left sums
                # more simplified view of below operation is 

                # discard_large_number = heapq.heappop(maxleft) * -1
                # leftsum += nums[i] - discard_large_number

                leftsum += nums[i] + heapq.heappop(maxheap) 
                heapq.heappush(maxheap, -nums[i])
            leftMins[i] = leftsum
        
        minheap = [] # this is for right partition
        rightSum = 0
        for i in range(2*n, len(nums)):
            heapq.heappush(minheap, nums[i])
            rightSum += nums[i]
        rightMaxs[i] = rightSum


        for i in range(n , len(nums) - n):
            if nums[i] > minheap[0]:
                rightSum += nums[i] - heapq.heappop(minheap)
                heapq.heappush(minheap, nums[i])
            rightMaxs[i] = rightSum
        

        minDiff = float('inf')
        print(leftMins, rightMaxs)
        for i in range(n - 1, len(nums) - n):
            minDiff = min(minDiff, leftMins[i] - rightMaxs[i + 1])

        return minDiff
        """



        # maxheap for right
        # min heap for left

        # we heapidy the nums array.
        # the first n elements will be smallest 
        # the second n elements are the one which we need to ignor

        
        # all this below bullshittery is kachara


        # def get_diff(exclude_idx:List[int]) -> int:
        #     first, second = 0, 0
        #     f_idx = 0
        #     idx = 0
        #     while f_idx < n:
        #         if idx in exclude_idx:
        #             idx += 1
        #             continue
        #         first += nums[idx]
        #         f_idx += 1
        #         idx += 1
            
        #     s_idx = 0

        #     while s_idx < n:
        #         if idx in exclude_idx:
        #             idx += 1
        #             continue
        #         second += nums[idx]
        #         s_idx += 1
        #         idx += 1
            
        #     return first -  second

        # # for i in range(len(nums)):
        # #     for j in range(i+1, len(nums)):
        # # get n eclude idx
        # n 
        # i = 0
        # while i < n:



        

            