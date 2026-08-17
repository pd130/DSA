#Time Complexity : O(N)
#Space : O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        most = max(seen.values())
        for i in seen:
            if seen[i] == most:
                return i

#Time : O(NlogN)
#Space : O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n== 1:
            return nums[0]
        n = n/2
        count = 0
        seen = 9999999999999999999999999999999999999
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == seen:
                count +=1
                if (count > n):
                    return nums[i]
            else:
                seen = nums[i]
                count = 1
        
#Optimal
#Time : O(N)
#Space : O(1)        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        candidate = nums[0]
        for i in range(1 , len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = nums[i]
                    count = 1

        return candidate
            
         


