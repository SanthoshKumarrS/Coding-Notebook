class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        result,sol = [] , []

        def backtrack(i):
            if i == n :
                result.append(sol[:])
                return
            
            #don't pick num[i]
            backtrack(i + 1)
            #pick nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)

        return result