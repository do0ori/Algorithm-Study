class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        answer = []
        comb = []

        def dfs(candidates, i, remain):
            if remain == 0:
                answer.append(comb.copy())
                return
            
            for nxt in range(i, N):
                if nxt > i and candidates[nxt] == candidates[nxt - 1]: continue
                if candidates[nxt] > remain: break;

                comb.append(candidates[nxt])
                dfs(candidates, nxt + 1, remain - candidates[nxt])
                comb.pop()
        
        dfs(candidates, 0, target)

        return answer