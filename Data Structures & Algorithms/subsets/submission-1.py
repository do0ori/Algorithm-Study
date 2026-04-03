class Solution:        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def bt(subset, i = 0):
            if i == len(nums):
                answer.append(subset)
                return
            
            bt(subset, i + 1)
            bt(subset + [nums[i]], i + 1)
        
        bt([]);

        return answer
