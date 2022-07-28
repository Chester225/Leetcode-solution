# Runtime: 55 ms, faster than 99.26% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 50.46% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in preMap:
                return[preMap[diff],i]
            preMap[n]=i
