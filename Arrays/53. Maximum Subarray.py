#Brute Force 
#Time : O(N^2)
#Space : O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            nums[i] = add
        max_sum = max(nums)
        for i in range(len(nums)):
            for j in range(i+1 ,len(nums)):
                if nums[j] - nums[i] > max_sum:
                    max_sum = nums[j] - nums[i]
        return max_sum

#Optimal
#Time : O(N)
#Space : O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -999999999999
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum > 0:
                curr_sum += nums[i]
            else:
                if curr_sum > nums[i]:
                    curr_sum += nums[i]
                else:
                    curr_sum = nums[i]
            if curr_sum > maximum:
                maximum = curr_sum
        return maximum

        
#Optimal #2
#Kadane's Algorithm
#Time : O(N)
#Space : O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i] , curr_sum + nums[i])
            maximum = max(curr_sum , maximum)
        return maximum

        
