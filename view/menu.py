import controller.controller as controller

def menu(nav: list):
    # Display the menu
    for i in range(len(nav)):
        print(f"[{i+1}] {nav[i]}")
    while True:
        
        go_to = controller.request(f"Navigasi ke halaman (1-{len(nav)})", ["required", "digit"])
        go_to = int(go_to)
        
        # Check if the input is in range
        if 1 <= go_to <= len(nav):
            return {
                "index": go_to - 1,
                "val": nav[go_to - 1]
            }
        
        print("Menu yang anda pilih tidak tersedia. Pilih nomor yang sesuai.\n")