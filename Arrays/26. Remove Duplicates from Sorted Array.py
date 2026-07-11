#Brute Force
# Time Complexity O(N^2)
# Space Complexity O(N)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniques = {}
        dupes = []
        for i in range(len(nums)):
            if nums[i] not in uniques.keys():
                uniques[nums[i]] = 1
            else:
                dupes.append(i)
            dupes.sort()
            dupes.reverse()
        for i in dupes:
            nums.pop(i)
        return len(nums)
        
#Brute Force #2
# Time Complexity O(N^2)
# Space Complexity O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j+=1
            if j <len(nums):
                nums[i+1 : j] = [nums[j]]*(j-i-1)
            else:
                break
        counter = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                counter+=1
        return counter+1
        
# Optimal
# Time Complexity O(N)
# Time Complexity O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1 , len(nums)):
            if nums[k-1] != nums[i]:
                nums[k] = nums[i]
                k+=1
            else:
                continue
        return k
                
            
        