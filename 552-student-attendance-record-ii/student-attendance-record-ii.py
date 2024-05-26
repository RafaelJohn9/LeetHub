class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize dp table with zeros
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        
        for i in range(1, n + 1):
            for A in range(2):
                for L in range(3):
                    # Adding 'P'
                    dp[i][A][0] += dp[i-1][A][L]
                    dp[i][A][0] %= MOD
                    
                    # Adding 'A'
                    if A > 0:
                        dp[i][A][0] += dp[i-1][A-1][L]
                        dp[i][A][0] %= MOD
                        
                    # Adding 'L'
                    if L > 0:
                        dp[i][A][L] += dp[i-1][A][L-1]
                        dp[i][A][L] %= MOD
        
        # Sum up all valid records of length n
        result = 0
        for A in range(2):
            for L in range(3):
                result += dp[n][A][L]
                result %= MOD
        
        return result
