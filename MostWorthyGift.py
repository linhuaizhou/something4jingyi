"""
date:20231128
author:lhz
note:Most Worthy Gift
"""


def max_gift_value(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = matrix[0][0]

    # 初始化第一行和第一列
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    # 动态规划递推
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    return dp[-1][-1]


mat = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

result = max_gift_value(mat)
print(result)
