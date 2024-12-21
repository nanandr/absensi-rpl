import re

def request (name: str, rules: list) -> str: # Rules: required, digit, date
    while True:
        val = input(f"{name}: ")
        if "required" in rules and val.strip() == "":
            print(f"{name} tidak boleh kosong.\n")
            continue
        if "digit" in rules and not val.isdigit():
            print(f"{name} harus berupa angka.\n")
            continue
        if "date" in rules:
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", val):
                print(f"{name} harus dalam format YYYY-MM-DD.\n")
                continue
            try:
                from datetime import datetime
                datetime.strptime(val, "%Y-%m-%d")
            except ValueError:
                print(f"{name} tidak valid. Gunakan format YYYY-MM-DD yang benar.\n")
                continue

        return val