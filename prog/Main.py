import csv
FILENAME = "file.csv"

users = [
        {"NAME": "Tom", "AGE": 28},
        {"NAME": "Alice", "AGE": 23},
        {"NAME": "Alice", "AGE": 23},
        {"NAME": "Bob", "AGE": 34}
    ]

with open(FILENAME, "w", newline="") as file:
        columns = ["NAME", "AGE"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        writer.writerows(users)

        user = {"NAME": "Sam", "AGE": 41}

        writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["NAME"], "-", row["AGE"])

    numstr1 = input("Enter two numbers of strings\n")
    numstr2 = input()

with open(FILENAME) as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        row1 = list()
        row2 = list()
        for row in reader:
            if i == int(numstr1):
                row1 = row
            if i == int(numstr2):
                row2 = row
            i += 1
        if row1 == row2:
            print("Strings are equals")
            print(row1)
            print(row2)
        else:
            print("Strings aren't equals")
            print(row1)
            print(row2)