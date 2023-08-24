class Solution:
    def longestPalindrome(self, s: str) -> str:
        word1 = s
        word2 = s[::-1]
        s1 = ""
        dp = [[0]*(len(word2)+1) for x in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if (word1[i-1] == word2[j-1]):
                    dp[i][j] = dp[i-1][j-1] + 1
                    s1 += word1[j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return s1
