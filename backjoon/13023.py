# 13023. ABCDE 
import sys
#재귀횟수 한도 늘리기
sys.setrecursionlimit(10000)

n = list(map(int, sys.stdin.readline().split()))
graph = {}

for i in range(0, n[0]):
    graph[i] = []

for i in range(0, n[1]):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

visited = [False] * n[0]
result = False

def recursive_dfs(v, depth):
    global result
    if depth >= 4:
        result = True
        return
    for w in graph[v]:
        if not visited[w]:
            visited[w] = True
            recursive_dfs(w, depth+1)
            visited[w] = False

for i in range(0, n[0]):
    visited[i] = True
    recursive_dfs(i, 0)
    visited[i] = False

if result:
    print(1)
else:
    print(0)