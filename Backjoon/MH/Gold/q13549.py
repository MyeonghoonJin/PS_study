"""
숨바꼭질 3 - g5
dijkstra
"""
import heapq
def solve():
    N,K = map(int,input().split())
    if K < N:
        print(N - K)
        return
    def dijkstra(start,end):
        INF = int(1e9)
        dist = [INF] * (10**6 + 1)
        dist[start] = 0
        min_heap = [(0,start)]
        while min_heap:
            # 현재 노드와 그 노드까지 최단 거리
            current_dist,u = heapq.heappop(min_heap)

            # 도착 시
            if u == end:
                return current_dist

            # 현재 거리가 저장된 거리보다 큰 경우 / u가 범위 밖의 값인 경우
            if current_dist > dist[u]:
                continue

            # 현재 노드의 인접한 노드들에 대해 최단거리 갱신
            dir = [1,-1]
            for i in dir:
                if 0 <= u + i <= 10**6 and current_dist + 1 < dist[u + i]:
                    dist[u + i] = current_dist + 1
                    heapq.heappush(min_heap,(dist[u + i],u + i))
            if 0 <= 2 * u <= 10**6 and current_dist < dist[2 * u]:
                dist[2 * u] = current_dist
                heapq.heappush(min_heap,(dist[2 * u],2 * u))
        return False

    print(dijkstra(N,K))

if __name__ == '__main__':
    solve()