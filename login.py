mahasiswa = [
    {
        "nama": "Nandana Rafi Ardika",
        "nim": 2404158,
        "password": "nanda123"
    },
    {
        "nama": "Muhammad Yasir Royyan",
        "nim": 2401266,
        "password": "yasir123"
    },
    {
        "nama": "Natasya Ramadhani",
        "nim": 2403264,
        "password": "natasya123"
    },
    {
        "nama": "Wisnu Firmansyah Handjoyo",
        "nim": 2404525,
        "password": "wisnu123"
    }
]

authenticated = False

while not authenticated:
    print("Login Sistem Absensi RPL")
    print("------------------------")
    nim = int(input("NIM: "))
    password = input("Password: ")
    print("------------------------")
    for i in range(len(mahasiswa)):
        if mahasiswa[i]["nim"] == nim:
            if mahasiswa[i]["password"] == password:
                print(f"Selamat datang {mahasiswa[i]["nama"]}")
                authenticated = True
                break
            else:
                print("Password yang anda isi salah \n")
                break
        elif i == len(mahasiswa)-1:
            print(f"Tidak dapat menemukan akun mahasiswa dengan NIM {nim} {i} \n")