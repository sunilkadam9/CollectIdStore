import os
import re

def find_ids_in_file(file_path):
    """
    Reads a file and extracts all 'id' occurrences using regular expressions.
    Assumes the 'id' is in the format 'id: <value>' or 'id = <value>'.
    """
    ids = []
    id_pattern = re.compile(r'\b(?:id[:=]\s*)(\w+)\b', re.IGNORECASE)

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            ids.extend(id_pattern.findall(content))
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

    return ids

def collect_ids(directory):
    """
    Recursively traverse the directory and subdirectories to find and collect all ids.
    """
    all_ids = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_ids = find_ids_in_file(file_path)
            all_ids.extend(file_ids)

    return all_ids

if _name_ == "_main_":
    directory = input("Enter the directory path to scan: ")
    ids = collect_ids(directory)
    print(f"Collected IDs: {ids}")
