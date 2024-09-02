def min_distance(word1: str, word2: str) -> int:
    n = len(word1)
    m = len(word2)

    memo = [[-1] * (m + 1) for _ in range(n + 1)]

    for i in range(m + 1):
        memo[n][i] = m - i

    for i in range(n + 1):
        memo[i][m] = n - i

    for i in range(n - 1,-1,-1):
        for j in range(m - 1,-1,-1):
            if word1[i] == word2[j]:
                memo[i][j] = memo[i + 1][j + 1]
            else:
                memo[i][j] = min(memo[i + 1][j + 1]), \
                memo[i + 1][j], memo[i][j + 1] + 1

    return memo[0][0]