#Brute Force 1
# Time Complexity : O(N)
# Space Complexity : O(N)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = nums.count(0)
        nums[:] = [x for x in nums if x != 0]
        nums += [0]*zero_count
        
        

                
#Brute Force 2
#Time Complexity : (worsrt case) O(N^2)
#Space Complexity : O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = nums.count(0)
        for i in range(len(nums)-1 , -1 , -1):
            if nums[i] == 0:
                nums.pop(i)
        nums += [0]*zero_count
        
        
# Optimal 
# Time Complexity : O(N)
# Space Complexity : O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] , nums[i] = nums[i] , nums[k]
                k += 1