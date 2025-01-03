import re

def request (name: str, rules: list) -> str: # Rules: required, digit, date
    while True:
        val = input(f"{name}: ")
        if "required" in rules and val.strip() == "":
            print(f"{name} tidak boleh kosong.\n")
            continue
        if "range" in rules:
            range_match = re.match(r"^(\d+)-(\d+)$", val)
            if not range_match:
                print(f"Input harus dalam format angka-angka, seperti '1-5'.\n")
                continue
            start, end = map(int, range_match.groups())
            if start > end:
                print(f"Rentang tidak valid: angka awal harus lebih kecil atau sama dengan angka akhir.\n")
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
        if "time" in rules:
            if not re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", val):
                print(f"{name} harus dalam format HH:MM (contoh: 14:30).\n")
                continue

        return val