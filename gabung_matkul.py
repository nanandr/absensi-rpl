from mata_kuliah import mata_kuliah

found = False

while not found:
    print("Gabung mata kuliah")
    kode = input("Kode: ")
    for i in range(len(mata_kuliah)):
        if mata_kuliah[i]["kode"] == kode:
            found = True
            print(f"Selamat datang di mata kuliah {mata_kuliah[i]["nama"]}")
            break
        elif i == len(mata_kuliah)-1:
            print("Tidak dapat menemukan mata kuliah \n")