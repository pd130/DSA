class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 1 and counter > k:
                    k = counter
                    counter = 0
            elif nums[i] != 1 and counter <= k:
                counter = 0
            else:
                counter += 1
        if counter>k:
            k = counter
        return k
                
        