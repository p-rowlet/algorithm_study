# 11724. 연결요소의 개수

import sys
#재귀횟수 한도 늘리기
sys.setrecursionlimit(10000)

n = list(map(int, sys.stdin.readline().split()))
cnt = [i+1 for i in range(0, n[0])]
count = 0

#그래프 생성하기
graph = {}

for i in range(1, n[0]+1):
    graph[i] = []

for i in range(0, n[1]):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

def recursive_dfs(v, discovered):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


# 그래프 순회
while(True):
    discover = []
    if not cnt:
        break
    recursive_dfs(cnt[0], discover)
    
    for i in discover:
        cnt.remove(i)
    count += 1

print(count)