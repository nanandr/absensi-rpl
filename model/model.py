from datetime import datetime
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
    match = []
    for item in data:
        if item.get(key) == val:
            match.append(item)
    return match

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

def get_time (param_time = None):
    if param_time:
        return datetime.strptime(param_time, "%H:%M").time()
    return datetime.now().time()

def get_day ():
    return datetime.now().weekday()

def get_date (param_date = None):
    if param_date:
        return datetime.strptime(param_date, "%Y-%m-%d").date()
    return datetime.now().date()