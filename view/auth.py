import view.view as view

def login () -> None:
    view.div("-")
    print("Login Sistem Absensi RPL")
    view.div("-")

def signup () -> None:
    view.div("-")
    print("Signup Sistem Absensi RPL")
    print("Buat Akun Mahasiswa")
    view.div("-")

def success (name: str) -> None:
    view.div("-")
    print(f"Selamat datang, {name}\n")