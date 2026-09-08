class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        nums_len = len(nums)
        res = []
        # print(nums)
        index_dict = {}
        for index, num in enumerate(nums):
            index_dict[num] = index

        i = 0
        prev = float('-inf')
        while i < nums_len-2:
            if nums[i] != prev:
                j = i + 1
                prev_j = float('-inf')
                while j < nums_len-1:
                    if nums[j] != prev_j:
                        target = -1 * (nums[i] + nums[j])

                        if target in index_dict and index_dict[target] > j:
                            # print(i, j, index_dict[target])
                            res.append([nums[i], nums[j], target])
                    prev_j = nums[j]
                    j += 1
            prev = nums[i]
            i += 1
        return res
