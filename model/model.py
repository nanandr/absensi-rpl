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