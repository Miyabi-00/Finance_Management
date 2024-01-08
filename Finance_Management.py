
import csv

file = f"Rakuten_all.csv"

with open(file, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        print(row)
