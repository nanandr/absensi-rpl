import view.login as view
import model.mahasiswa

def login () -> bool:
    authenticated = False
    while not authenticated:
        view.login()    
        nim, password = "", ""
        while nim == "":
            nim = input("NIM: ")
            if nim.strip() == "":
                view.fail("NIM tidak boleh kosong")

        while password == "":
            password = input("Password: ")
            if password.strip() == "":
                view.fail("Password tidak boleh kosong")

        mahasiswa = model.mahasiswa.find("nim", nim)
        if len(mahasiswa) > 0:
            if mahasiswa[0]["password"] == password:
                authenticated = True
                view.success(mahasiswa[0]["name"])
            else:
                view.fail("Password yang anda isi salah")
        else:
            view.fail("NIM yang anda isi tidak tersedia")
        
    return authenticated