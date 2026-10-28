# Pertemuan 12 — File Input-Output dan Penanganan Error Dasar Python

## Identitas

- **Nama:** Ahmad Nurikhsan
- **NIM:** 2225250042
- **Kelas:** 3E
- **Program Studi:** S1 Pendidikan Matematika
- **Mata Kuliah:** Algoritma dan Pemrograman

## Deskripsi

Praktikum ini membahas penggunaan file untuk menyimpan dan membaca data menggunakan Python, menambahkan isi file, memproses data per baris, serta menangani kesalahan dasar seperti file tidak ditemukan dan input yang bukan angka.

## Struktur Folder

```text
pertemuan-12-file-io-2225250042/
├── README.md
├── .gitignore
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
└── tugas/
    └── rekap_nilai_file.py
```

## Daftar Latihan

1. `01_tulis_file.py` — menulis data ke dalam file teks.
2. `02_baca_file.py` — membaca isi file teks.
3. `03_append_file.py` — menambahkan data ke file.
4. `04_proses_baris.py` — membaca dan memproses data per baris.
5. `05_file_not_found.py` — menangani kesalahan ketika file tidak ditemukan.
6. `06_value_error.py` — menangani input yang tidak dapat dikonversi menjadi angka.

## Tugas Utama: Rekap Nilai

Program `rekap_nilai_file.py` membaca data mahasiswa dari `data/nilai.txt`, memproses nilai yang valid, lalu menghitung jumlah data valid, rata-rata, nilai minimum, nilai maksimum, dan jumlah nilai yang mencapai batas kelulusan 60.

### Format Input

Setiap baris berisi NIM dan nilai yang dipisahkan dengan tanda koma.

Contoh:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Baris kosong dan data dengan format atau nilai yang tidak valid dilewati.

### Cara Menjalankan

Jalankan perintah berikut dari folder utama proyek:

```bash
python tugas/rekap_nilai_file.py
```

### Hasil Rekap

Untuk data contoh di atas, hasil rekap yang diharapkan adalah:

```text
Jumlah data valid: 5
Rata-rata: 83.40
Minimum: 74.00
Maksimum: 92.00
Jumlah lulus: 5
```

Hasil rekap disimpan dalam file `data/hasil_rekap.txt`.

## Pengujian

- Menguji penulisan dan pembacaan file teks.
- Menguji penambahan isi file.
- Menguji pemrosesan data nilai per baris.
- Menguji penanganan file yang tidak ditemukan.
- Menguji input nilai yang bukan angka.
- Menguji rekap nilai dengan data valid dan tidak valid.

## Refleksi

Melalui praktikum ini, saya mempelajari cara membaca, menulis, dan menambahkan data pada file teks menggunakan Python. Saya juga mempelajari cara memproses data per baris serta menangani kesalahan menggunakan `try-except`. Materi ini membantu saya memahami pengolahan data yang tersimpan dalam file.

