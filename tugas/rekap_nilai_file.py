def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data.append((nim.strip(), nilai))

                except ValueError:
                    print(f"Baris {nomor} dilewati: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai = [item[1] for item in data]

    jumlah_data = len(nilai)
    rata_rata = sum(nilai) / jumlah_data
    nilai_minimum = min(nilai)
    nilai_maksimum = max(nilai)
    jumlah_lulus = sum(1 for x in nilai if x >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {nilai_minimum:.2f}\n")
        file.write(f"Maksimum: {nilai_maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")

    print(f"Rekap ditulis ke {nama_file}")
    print(f"Jumlah data valid: {jumlah_data}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Minimum: {nilai_minimum:.2f}")
    print(f"Maksimum: {nilai_maksimum:.2f}")
    print(f"Jumlah lulus: {jumlah_lulus}")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)
if data:
    tulis_rekap(output_file, data)