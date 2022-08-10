# 11047. 동전 0
import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
coin_count = 0
pointer = n-1

for i in range(0, n):
    coin.append(int(sys.stdin.readline()))

while(k > 0):
    tmp = k // coin[pointer]
    coin_count += tmp
    k %= coin[pointer]
    pointer -= 1

    if pointer == -1:
        break

print(coin_count)