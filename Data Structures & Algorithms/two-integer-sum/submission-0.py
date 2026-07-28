class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        dicti = {}
        for i in range(len(nums)):
            complementary = t - nums[i] 
            if complementary in dicti:
                return [dicti[complementary], i]
            dicti[nums[i]] = i