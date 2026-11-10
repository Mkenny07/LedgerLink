import csv

with open("data/orders.csv", "r") as file:
    orders = csv.DictReader(file)

    for order in orders:
        print(order)
