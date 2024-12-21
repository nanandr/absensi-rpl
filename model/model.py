import csv
import os

def fetch (items: list) -> list:
    reader = csv.DictReader(items)
    return [row for row in reader]

def read (path: str) -> list:
    if os.path.exists(path):
        data = []

        with open(path, "r") as file:
            data = fetch(file)
        
        return data
    
def find (path: str, key: str, val: any) -> list:
    data = read(path)
    for item in data:
        if item.get(key) == val:
            return [item]
    return []

def save (path: str, data: list) -> list:
    fieldNames = data[0].keys()

    with open(path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(data)

def append(path: str, data: list) -> list:
    fieldNames = data[0].keys()
    
    # Check if file exists and is non-empty
    file_exists = os.path.exists(path) and os.path.getsize(path) > 0

    with open(path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        if not file_exists:  # Write header only if the file is new or empty
            writer.writeheader()
        writer.writerows(data)