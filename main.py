from login import login

def main ():
    authenticated = False
    while not authenticated:
        print("Login Sistem Absensi RPL")
        print("------------------------")
        nim = int(input("NIM: "))
        password = input("Password: ")
        print("------------------------")

        res = login(nim, password)
        authenticated = res["authenticated"]
    
    user = res["mahasiswa"] #Dictionary akun mahasiswa
    
        
main()