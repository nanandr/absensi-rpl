print("=============================================================")
print("\t\tSistem Absensi [PJ Matkul]")
print("")
print("\t\tRekayasa Perangkat Lunak")
print("\t    Universitas Pendidikan Indonesia")
print("=============================================================")

absensi = {}

while True:
    print("\nMasukkan urutan absen:")
    print("1. Input absensi satu persatu (contoh: 1)")
    print("2. Input absensi bulk (contoh: 1-18)")
    pilihan = input("Pilihan (1/2): ")

    if pilihan == '1': 
        absen = int(input("Masukkan nomor absen: "))
        if absen <= 0:
            print("Mohon masukkan nomor absen yang valid (contoh: 5)")
            break
        else:
            absensi[absen] = "Hadir"
            print(f"Data absensi mahasiswa dengan nomor absen {absen} telah diinput.")

    elif pilihan == '2': 
        start = int(input("Masukkan nomor awal: "))
        end = int(input("Masukkan nomor akhir: "))
        if start > end or (start <= 0 and end <= 0):
            print("Tidak valid. Pastikan start <= end dan bernilai positif!")
        else:
            for i in range(start, end + 1):
                absensi[i] = "Hadir"
            print(f"Data absensi mahasiswa nomor absen {start}-{end} telah diisi 'Hadir'.")
    
    else:
        print("Pilihan tidak valid. Pilih 1 atau 2.")
    ubah = input("\nApakah Anda ingin mengubah absensi untuk salah satu mahasiswa? (y/n): ").lower()
    if ubah == 'y':
        nomor_ubah = int(input("Masukkan nomor absen mahasiswa yang ingin diubah: "))
        if nomor_ubah not in absensi:
            print(f"Mahasiswa nomor {nomor_ubah} belum diinput sebagai Hadir atau Tidak Hadir. Silakan isi absensi dulu!")
        else:
            status_baru = input(f"Masukkan status baru untuk mahasiswa nomor {nomor_ubah} (Hadir/Tidak Hadir): ")
            absensi[nomor_ubah] = status_baru
            print(f"Absensi mahasiswa nomor {nomor_ubah} berhasil diubah menjadi '{status_baru}'.")
    lanjut = input("\nApakah Anda ingin menambah data absensi lagi? (y/n): ").lower()
    if lanjut != 'y':
        break
print("\nHasil Absensi:")
for no_absen, status in sorted(absensi.items()):
    print(f"Mahasiswa {no_absen}: {status}")
print("Absensi selesai.")