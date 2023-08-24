class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb(i, target, ds, ans):
            if i == len(candidates):
                if target == 0 and ds not in ans:
                    ans.append(ds.copy())
                return
            if candidates[i] <= target:
                ds.append(candidates[i])
                comb(i, target - candidates[i], ds, ans)
                ds.pop()
            comb(i + 1, target, ds, ans)
            return ans
        return comb(0, target, ds = [], ans = [])
