from utils import hitung_waktu


def cari_semua_rute(graph, start, end, hambatan_map):
    all_paths = []
    start = start.lower()
    end = end.lower()

    def dfs(current, path, visited):
        visited.add(current)
        path.append(current)

        if current == end:
            total_jarak = 0
            total_waktu = 0

            for i in range(len(path) - 1):
                kota1, kota2 = path[i], path[i + 1]
                jarak = graph[kota1][kota2]["jarak"]

                hambatan = hambatan_map.get(f"{kota1}-{kota2}") or \
                    hambatan_map.get(f"{kota2}-{kota1}") or {}

                macet = hambatan.get("macet", 0.0)
                rusak = hambatan.get("jalan_rusak", 0.0)

                total_jarak += jarak
                total_waktu += hitung_waktu(jarak, macet, rusak)

            all_paths.append({
                "rute": path.copy(),
                "total_jarak": total_jarak,
                "total_waktu": round(total_waktu, 2)
            })
        else:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    dfs(neighbor, path, visited)

        path.pop()
        visited.remove(current)

    dfs(start, [], set())

    # Urutkan semua rute berdasarkan waktu tempuh
    sorted_rute = sorted(all_paths, key=lambda x: x["total_waktu"])

    # Pastikan rute langsung (start → end) muncul pertama jika ada
    direct_key = [start, end]
    sorted_rute.sort(key=lambda x: x["rute"][:2] != direct_key)

    return sorted_rute
