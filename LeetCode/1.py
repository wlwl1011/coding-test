class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            check = nums[i]
            for j in range(i+1,len(nums)):
                if check+nums[j] == target:
                    answer = [i,j]
                    break
        return answer