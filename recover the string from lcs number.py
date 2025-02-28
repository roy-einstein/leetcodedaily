def longestCommonSubsequence(text1: str, text2: str) -> str:
    m, n = len(text1), len(text2)

    # Step 1: Create DP table (m+1) x (n+1) initialized to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill the DP table (Bottom-up DP)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:  # Match case
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:  # No match case
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 3: Backtrack to reconstruct LCS string
    i, j = m, n
    lcs = []

    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:  # If characters match, add to LCS
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Move up
            i -= 1
        else:  # Move left
            j -= 1

    return "".join(reversed(lcs))  # Reverse to get correct LCS order

# Example usage:
text1 = "abac"
text2 = "cab"
print(longestCommonSubsequence(text1, text2))  # Output: "ab"
