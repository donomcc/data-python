import csv
open_file = open("CupcakeInvoices.csv")
reader = csv.reader(open_file)

total = 0

for line in open_file:
    # print(line) prints each row
    line = line.strip()
    values = line.split(",")
    # print(values[2]) prints the cupcake type

open_file.seek(0)

for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values[4])
    total += float(values[4])

print("Total is:",total)

open_file.close()