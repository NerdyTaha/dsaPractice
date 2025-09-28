class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #last_index = len(nums) - 1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                addition = nums[i] + nums[j]
                if addition == target:
                    answer = [i,j]
                    return answer
