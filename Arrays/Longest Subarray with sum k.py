#Time O(N^2)
#Space O(1)
class Solution:
    def longestSubarray(self, arr, k):  
        add = 0
        length = 0
        for i in range(len(arr)):
            add += arr[i]
            arr[i] = add
            if arr[i] == k:
                if i+1 > length:
                    length = i+1
        for i in range(len(arr)):
            for j in range(i+1 , len(arr)):
                if (arr[j] - arr[i]) == k:
                    if (j-i+1) > length:
                        length = j-i
        return length

#Time O(N)
#Space O(N)
class Solution:
    def longestSubarray(self, arr, k):  
        seen = {0 : -1}   # IMP
        length = 0
        add = 0
        for i in range(len(arr)):
            add += arr[i]
            if add-k in seen:
                length = max(length ,i - seen[add-k])
            if add not in seen:  # IMP
                seen[add] = i
            arr[i] = add
        return length

                    
                