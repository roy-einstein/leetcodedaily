def missingWords(s, t):
    s_list = s.split()
    t_list = t.split()
    j = 0
    missing = []

    for word in s_list:
        if j < len(t_list) and word == t_list[j]:
            j += 1
        else:
            missing.append(word)

    return missing


from functools import cache


def getSubsequenceCount(s1, s2):
    # Write your code here
    s1, s2 = s2, s1
    m = len(s1)
    n = len(s2)

    @cache
    def dfs(s1, s2, m, n):
        if (m == 0 and n == 0) or n == 0:
            return 1
        if m == 0:
            return 0;

        if s1[m - 1] == s2[n - 1]:
            return dfs(s1, s2, m - 1, n - 1) + dfs(s1, s2, m - 1, n)
        else:
            return dfs(s1, s2, m - 1, n)
    return dfs(s1, s2, m, n)

def getSubsequenceCount(s1, s2):
    m, n = len(s1), len(s2)

    dp =[[0]* (n+1) for _ in range(m +1)]

    for j in range(n+1):
        dp[0][j] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] +dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    return dp[m][n]

if __name__ == "__main__":
    s="Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing"
    t="Python is an easy to learn powerful programming language"
    # b= missingWords(s, t)
    # print(b)

    s1="ELO"
    s2= "HELLOWORLD"

    b=getSubsequenceCount(s1,s2)
    print(b)
