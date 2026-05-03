wt = [5, 15, 25]
val = [60, 90, 140]
W = 40

n = len(val)

dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):
        if wt[i - 1] <= w:
            dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

print("Max Profit:", dp[n][W])