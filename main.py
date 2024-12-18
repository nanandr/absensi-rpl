from controller.login import login
import view.welcome

def menu(nav: list):
    while True:
        # Display the menu
        for i in range(len(nav)):
            print(f"[{i+1}] {nav[i]}")
        
        go_to = input(f"Navigasi ke halaman (1-{len(nav)}): ").strip()
        
        # Check if input is a digit
        if not go_to.isdigit():
            print("Harap masukkan angka yang valid.\n")
            continue
        
        go_to = int(go_to)
        
        # Check if the input is in range
        if 1 <= go_to <= len(nav):
            return nav[go_to - 1]
        
        print("Menu yang anda pilih tidak tersedia. Pilih nomor yang sesuai.\n")

def main ():
    authenticated = False

    # Before login
    while not authenticated:
        view.welcome.guest()

        nav = menu(["Login", "Register", "Exit"])
        if nav == "Login":
            if login():
                authenticated = True
        elif nav == "Register":
            pass
        elif nav == "Exit":
            break

    while authenticated:
        view.welcome.user()

        nav = menu(["Buat Mata Kuliah", "Gabung Mata Kuliah", "Logout"])

        if nav == "Logout":
            authenticated = False
            break
    
main()