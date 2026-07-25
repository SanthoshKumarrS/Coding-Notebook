class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        current_sum = 0

        for i in range(k):
            current_sum += nums[i]
            max_avg = current_sum / float(k)
        
        for i in range(k, n):
            current_sum += nums[i]
            current_sum -= nums[i - k]

            avg = current_sum / float(k)
            max_avg = max(max_avg, avg)
        
        return max_avg