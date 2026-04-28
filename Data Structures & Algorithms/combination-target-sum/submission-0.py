class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, comb, total):
            # 가지치기
            if total > target:
                return
            
            # 종료조건
            if total == target:
                answer.append(comb)
                return
            
            for nxt in range(i, len(nums)):
                dfs(nxt, comb + [nums[nxt]], total + nums[nxt])

            
        answer = []
        dfs(0, [], 0)
        return answer