#Brute Force  # Hashing
#Time Complexity : O(N)
#Space Complexity : O(N)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return nums[0]
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i in seen.keys():
            if seen[i] == 1:
                return i
    
#Optimal  #Bit Manipulation
#Time Complexity : O(N)
#Space Complexity  : O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return nums[0]
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i in seen.keys():
            if seen[i] == 1:
                return i
    
        
        
        