# 1260. DFS와 BFS

import sys
#재귀횟수 한도 늘리기
sys.setrecursionlimit(10000)

n = list(map(int, sys.stdin.readline().split()))
graph = {}

for i in range(1, n[0]+1):
    graph[i] = []

for i in range(0, n[1]):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

for i in range(1, n[0]+1):
    graph[i].sort()

def recursive_dfs(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

def bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

print(* recursive_dfs(n[2]))
print(* bfs(n[2]))