matkul  = [
    {
        "nama matkul": "Pengantar Rekayasa Perangkat Lunak",
        "kode matkul": "RL116",
        "dosen"      : "Dian Anggraeni, S.ST, M.T",
        "kode dosen" : 3082,
        "sks"        : 3,
        "pj"         : "Mahesa Syawal Abdurrahman",
    },
    {
        "nama matkul": "Literasi Teknologi Informasi & Komunikasi",
        "kode matkul": "RL115",
        "dosen"      : "Yulia Retnowati, S.Pd, M.T",
        "kode dosen" : 3442,
        "sks"        : 3,
        "pj"         : "Niranti Salma Nabilah",
    },
    {
        "nama matkul": "Dasar Pemrograman",
        "kode matkul": "RL117",
        "dosen"      : "Indira Syawanodya, S.Kom, M.Kom",
        "kode dosen" : 3081,
        "sks"        : 4,
        "pj"         : "Dwi Raisah Anandifa Kautsar",
    },
    {
        "nama matkul": "Matematika Dasar",
        "kode matkul": "RL118",
        "dosen"      : "Fahmi Candra Permana S.Si",
        "kode dosen" : 2993,
        "sks"        : 4,
        "pj"         : "Ilyasa Putra",
    },
    {
        "nama matkul": "Pendidikan Bahasa Indonesia",
        "kode matkul": "KU106",
        "dosen"      : "Yayang Furi Furnamasari, M.Pd",
        "kode dosen" : 3146,
        "sks"        : 2,
        "pj"         : "Mukhammad Vicky",       
    },
    {
        "nama matkul": "Pendidikan Pancasila",
        "kode matkul": "KU106",
        "dosen"      : "Fully Rakhmayanti, M.Pd",
        "kode dosen" : 3216,
        "sks"        : 2,
        "pj"         : "Wisnu Firmansyah Handjoyo",
    },
    {
        "nama matkul": "Pendidikan Agama islam",
        "kode matkul": "KU100",
        "dosen"      : "Dr. Jenuri, S.Ag, M.Pd",
        "kode dosen" : 2449,
        "sks"        : 2,
        "pj"         : "Resti Fujianti"
    }
]

# input ( kode kelas )
found = False

while not found:
    print("Gabung mata kuliah")
    kode = input("Kode: ")
    for i in range(len(matkul)):
        if matkul[i]["kode matkul"] == kode:
            found = True
            print(f"Selamat datang di mata kuliah {matkul[i]["nama matkul"]}")
            break
        elif i == len(matkul)-1:
            print("Tidak dapat menemukan mata kuliah \n")