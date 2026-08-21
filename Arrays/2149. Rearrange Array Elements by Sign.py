#Optimal
#Time : O(N)
#Space : O(N)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for i in nums:
            if i > 0:
                positive.append(i)
            else:
                negative.append(i)
        p = 0
        n = 0
        for i in range(len(nums)):
            if i%2 ==0:
                nums[i] = positive[p]
                p += 1
            else:
                nums[i] = negative[n]
                n+= 1
        return nums
        