import json

KECEPATAN_RATA2 = 60  # km/jam


def hitung_waktu(jarak, hambatan_macet=0.0, hambatan_jalan=0.0):
    total_hambatan = hambatan_macet + hambatan_jalan
    waktu_jam = jarak / KECEPATAN_RATA2
    return round(waktu_jam * 60 * (1 + total_hambatan), 2)


def load_hambatan(file_path="data/traffic.json"):
    try:
        with open(file_path, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else {}
    except (FileNotFoundError, json.JSONDecodeError):
        print("[Peringatan] Gagal memuat data hambatan, menggunakan default (kosong).")
        return {}


def validasi_kota(nama_kota, graph):
    return nama_kota.lower() in graph
