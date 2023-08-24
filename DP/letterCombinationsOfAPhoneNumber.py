class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def solve(i, curr):
            if (len(curr) == len(digits)):
                res.append(curr)
                return
            for char in hashMap[digits[i]]:
                solve(i + 1, curr + char)
        if (digits):
            solve(0, "")
        return res
