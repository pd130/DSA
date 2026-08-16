#Brute Force
#Time Complexity : O(N^2)
#Space Complexity : O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans
#Optimal Solution
#Time : O(N)
#Space : O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            if nums[i] in sums:
                sums[nums[i]] += [i]
            if nums[i] not in sums:
                sums[target-nums[i]] = [i] 
        for i in sums.keys():
            if len(sums[i]) == 2:
                return sums[i]