import view.auth
import controller.controller as controller
import model.mahasiswa

def signup () -> bool:
    authenticated = False
    user = {}
    
    while not authenticated:
        view.auth.signup()    
        
        nim = controller.request("NIM", ["required", "digit"])
        nama = controller.request("Nama", ["required"])
        password = controller.request("Password", ["required"])

        mahasiswa = model.mahasiswa.create(nama, nim, password)

        if len(mahasiswa) > 0:
            if mahasiswa[0]["password"] == password:
                authenticated = True
                user = mahasiswa[0]
                view.auth.success(user["nama"])
            else:
                print("Password yang anda isi salah.\n")
        else:
            print("NIM yang anda isi sudah terdaftar.\n")
        
    return {
        "auth": authenticated,
        "user": user
    }

def login ():
    authenticated = False
    user = {}
    
    while not authenticated:
        view.auth.login()    
        
        nim = controller.request("NIM", ["required", "digit"])
        password = controller.request("Password", ["required"])

        mahasiswa = model.mahasiswa.find("nim", nim)
        
        if len(mahasiswa) > 0:
            if mahasiswa[0]["password"] == password:
                authenticated = True
                user = mahasiswa[0]
                view.auth.success(user["nama"])
            else:
                print("Password yang anda isi salah.\n")
        else:
            print("NIM yang anda isi tidak tersedia.\n")
        
    return {
        "auth": authenticated,
        "user": user
    }