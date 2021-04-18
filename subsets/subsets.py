class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        possibilities = ["{0:b}".format(i).zfill(len(nums)) for i in range(2 ** len(nums))]
        ans = []
#         for i in range(2 ** len(nums)):
# #             Generate string using i
#             val = "{0:b}".format(i)
#             possibilities.append(val.zfill(len(nums)))
        # for i, word in enumerate(possibilities):
        #     temp = []
        #     for j in word:
        #         if int(j):
        #             temp.append(nums[int(j)])
        #     ans.append(temp)
        for combo in possibilities:
            temp = []
            for index, c in enumerate(combo):
                if c == '1':
                    temp.append(nums[index])
            ans.append(temp)
        return ans