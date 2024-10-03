import os
from pathlib import Path

mapping_parent_path = Path(
    "C:/Users/user/Desktop/Work Related/Labs SRF/Mapping Related"
)


import csv


def read_csv(file_path):
    with open(file_path, mode="r", newline="") as file:
        csv_reader = csv.reader(file)

        # Extracting the header
        header = next(csv_reader)
        print(f"Header: {header}")

        # Extracting the rows
        rows = []
        for row in csv_reader:
            rows.append(row)
            print(row)

    return header, rows


for content in mapping_parent_path.rglob("*.csv"):

    print(content)

    header, rows = read_csv(content)
