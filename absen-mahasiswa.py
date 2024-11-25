print("=============================================================")
print("\t\tSistem Absensi [Mahasiswa]")
print("")
print("\t\tRekayasa Perangkat Lunak")
print("\t    Universitas Pendidikan Indonesia")
print("=============================================================")

absensi = {}

def tambah_absen():
    nama = input("Masukkan nama: ")
    tanggal = input("Masukkan tanggal (dd-mm-yyyy): ")
    status = input("Masukkan status (Hadir/Tidak Hadir): ")
    
    if nama in absensi:
        absensi[nama].append({"tanggal": tanggal, "status": status})
    else:
        absensi[nama] = [{"tanggal": tanggal, "status": status}]
    print(f"Data absensi untuk {nama} telah ditambahkan.")

while True:
    print("\nMenu:")
    print("1. Tambah Absen")
    print("2. Keluar")
    
    pilihan = input("Pilih opsi (1/2): ")
    
    if pilihan == "1":
        tambah_absen()
    elif pilihan == "2":
        print("Logging out of program")
        break
    else:
        print("Opsi tidak valid. Pilih (1/2)")