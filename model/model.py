import os

def fetch (items: list) -> list:
    data = []
    keys = items[0].strip().split(",") # get the keys from the first row
    
    for i in range(1, len(items)):
        rows = items[i].strip().split(",") # get each columns
        data.append(dict(zip(keys, rows))) # map values according to keys
    
    return data

def read (path: str) -> list:
    if os.path.exists(path):
        data = []

        with open(path, "r") as file:
            data = fetch(file.readlines())
        
        return data