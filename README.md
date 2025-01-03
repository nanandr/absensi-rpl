# Sistem Absensi
Kelompok 4 - RPL 1C
* Nandana Rafi Ardika - 2404158
* Muhammad Yasir Royyan - 2401266
* Natasya Ramadhani - 2403264
* Wisnu Firmansyah Handjoyo - 2404525

## Fitur
* **Absen**
* **Rekap Absen**

## Pengguna
### Penanggung Jawab Mata Kuliah
* **Buat Mata Kuliah** - PJ mampu mendaftarkan mata kuliah dan mengundang mahasiswa
* **Edit Mata Kuliah** - PJ mampu mengubah data mata kuliah
* **Kelola Absen** - PJ mampu mengelola absensi mahasiswa, termasuk menambahkan, mengubah, dan rekap data absensi

### Mahasiswa
* **Gabung Mata Kuliah** - 
* **Absen** - Mahasiswa mampu mengisi absen di mata kuliah yang sudah di kontrak
* **Rekap Absen** - Mahasiswa dapat melihat rekap absen yang sudah di isi selama perkuliahan berlangsung

## Konfigurasi
Aplikasi Sistem Absensi dapat disesuaikan dengan kebutuhan dengan memodifikasi file
```sh
config.json
```
```sh
{
    "university_name": (string),
    "start_semester": (list),
    "total_weeks": (int)
}
```
* **university_name** - Nama Instansi
* **start_semester** - List untuk menentukan tanggal mulai semester ("MM-DD") dalam bentuk list [ganjil, genap]
* **total_weeks** - Total pertemuan selama 1 semester

## Menjalankan Aplikasi
Dalam terminal, jalankan perintah
```sh
python main.py
```