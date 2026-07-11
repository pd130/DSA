#Brute Force
#Time Complexity : O(N^2)
#Space Complexity : O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            j = nums.pop(-1)
            nums.insert(0 , j)
            
#Optimal #1
#Time Complexity : O(N)
#Space Complexity : O(N)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        orignal = nums[:]
        for i in range(0 , len(nums)):
            nums[(i+k)%length] = orignal[i]
        
#Optimal #2
# Time Complexity : O(N)
# Space Complexity : O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
