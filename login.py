from mahasiswa import mahasiswa

def login (nim: int, password: str) -> dict:
    for i in range(len(mahasiswa)):
        if mahasiswa[i]["nim"] == nim:
            if mahasiswa[i]["password"] == password:
                print(f"Selamat datang {mahasiswa[i]["nama"]}")
                return {
                    "authenticated": True,
                    "mahasiswa": mahasiswa[i]
                }
            else:
                print("Password yang anda isi salah \n")
                return { "authenticated": False }
        elif i == len(mahasiswa)-1:
            print(f"Tidak dapat menemukan akun mahasiswa dengan NIM {nim}\n")
            return { "authenticated": False }