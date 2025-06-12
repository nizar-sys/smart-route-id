import heapq
from utils import hitung_waktu


def dijkstra(graph, start, goal, hambatan_map):
    start = start.lower()
    goal = goal.lower()

    queue = [(0, start, [])]
    visited = set()

    while queue:
        total_waktu, current, path = heapq.heappop(queue)

        if current in visited:
            continue
        visited.add(current)

        path = path + [current]

        if current == goal:
            total_jarak = sum(graph[path[i]][path[i+1]]["jarak"]
                              for i in range(len(path)-1))
            return {
                "rute": path,
                "total_waktu": round(total_waktu, 2),
                "total_jarak": total_jarak
            }

        for neighbor, info in graph[current].items():
            jarak = info["jarak"]
            hambatan = hambatan_map.get(f"{current}-{neighbor}", 0)
            waktu = hitung_waktu(jarak, hambatan)
            heapq.heappush(queue, (total_waktu + waktu, neighbor, path))

    return None
