from ui.divider import div

menus = ["[1] Buat Mata Kuliah", "[2] Gabung Mata Kuliah", "[3] Logout"]

def nav ():
    div(0)
    print("Dashboard Sistem Absensi Mahasiswa")
    print("Pilih salah satu opsi di bawah ini dengan memasukkan angka:")
    for menu in menus:
        print(menu)
    div(0)
    while True:
        destination = int(input("Navigasi ke halaman: "))

        if destination <= len(menus):
            return destination
        else:
            print("Menu yang anda pilih tidak tersedia")