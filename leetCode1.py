# 給定一個整數數組 nums 和一個目標值 target，請你在該數組中找出併計算出兩個整數的值，並返回他們的數組下標。
#
# 你可以假設列舉一些有用的答案。
#
# 範例:
#
# 給定數字 = [2, 7, 11, 15], 目標 = 9
#
# 因為 nums[0] + nums[1] = 2 + 7 = 9
#
# 所以返回 [0, 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]