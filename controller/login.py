import view.login as view
import controller.controller as controller
import model.mahasiswa

def login () -> bool:
    authenticated = False
    user = {}
    
    while not authenticated:
        view.login()    
        
        nim = controller.request("NIM", ["required", "digit"])
        password = controller.request("Password", ["required"])

        mahasiswa = model.mahasiswa.find("nim", nim)
        
        if len(mahasiswa) > 0:
            if mahasiswa[0]["password"] == password:
                authenticated = True
                user = mahasiswa[0]
                view.success(user["nama"])
            else:
                print("Password yang anda isi salah.\n")
        else:
            print("NIM yang anda isi tidak tersedia.\n")
        
    return {
        "auth": authenticated,
        "user": user
    }