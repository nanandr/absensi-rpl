import view.view as view

def login () -> dict:
    view.div("-")
    print("Login Sistem Absensi RPL")
    view.div("-")

def success (name: str) -> None:
    view.div("-")
    print(f"Selamat datang, {name}\n")