D, H, W = map(int, input().split())
S_sq = D ** 2 / (H ** 2 + W ** 2)
print(int(H * S_sq ** 0.5), int(W * S_sq ** 0.5))
