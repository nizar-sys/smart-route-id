from graph import load_graph
from utils import load_hambatan, validasi_kota
from routes import cari_semua_rute


def main():
    graph = load_graph()
    hambatan = load_hambatan()
    
    daftar_kota = [k.title() for k in graph.keys()]
    print("Kota tersedia:", ", ".join(daftar_kota))

    start = input("Masukkan titik awal: ").lower()
    end = input("Masukkan titik tujuan: ").lower()

    if not validasi_kota(start, graph) or not validasi_kota(end, graph):
        print("Kota tidak ditemukan dalam data graf.")
        return

    hasil_semua = cari_semua_rute(graph, start, end, hambatan)

    if not hasil_semua:
        print("Tidak ditemukan rute yang valid.")
        return

    top_rute = hasil_semua[:4]

    print(f"\nMenampilkan rute dari {start.title()} ke {end.title()}:\n")

    rute_utama = top_rute[0]
    alternatif_lain = top_rute[1:4]

    selisih_signifikan = all(
        rute_utama["total_waktu"] > alt["total_waktu"] for alt in alternatif_lain)

    if selisih_signifikan:
        rute_str = " → ".join([k.title() for k in rute_utama["rute"]])
        print(f"   Rute: {rute_str}")
        print(f"   Jarak: {rute_utama['total_jarak']} KM")
        print(f"   Estimasi waktu: {rute_utama['total_waktu']} menit\n")

        print(f"   ===Alternatif lain yang mungkin lebih cepat===\n")
        for i, rute in enumerate(alternatif_lain, 1):
            rute_str = " → ".join([k.title() for k in rute["rute"]])
            print(f"{i}. Rute: {rute_str}")
            print(f"   Jarak: {rute['total_jarak']} KM")
            print(f"   Estimasi waktu: {rute['total_waktu']} menit\n")
    else:
        for i, rute in enumerate(top_rute[:3], 1):
            rute_str = " → ".join([k.title() for k in rute["rute"]])
            print(f"{i}. Rute: {rute_str}")
            print(f"   Jarak: {rute['total_jarak']} KM")
            print(f"   Estimasi waktu: {rute['total_waktu']} menit\n")


if __name__ == "__main__":
    main()
