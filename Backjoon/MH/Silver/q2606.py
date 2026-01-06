"""
바이러스
"""

import sys
input = sys.stdin.readline


node_count = int(input())

nodes = []
for i in range(node_count):
    nodes.append(i + 1)

edge_count = int(input())
edges = []
for _ in range(edge_count):
    a,b = map(int,input().split())
    edges.append((a,b))

visited = [False]*node_count

result = 0
added_nodes = []

def dfs(node):
    global result
    global added_nodes
    visited[node - 1] = True
    if node != 1:
        result += 1
        added_nodes.append(node)
    for x,y in edges:
        if x == node:
            if not visited[y - 1]:
                dfs(y)
        elif y == node:
            if not visited[x - 1]:
                dfs(x)

dfs(1)
print(result)