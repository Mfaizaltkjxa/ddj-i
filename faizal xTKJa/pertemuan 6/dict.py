belanja = [
    {"buah":"Semangka", "harga":12000},
    {"buah":"Nanas", "harga":10000},
    {"buah":"Pepaya", "harga":12000},
    ]

total_belanja = 0
for item in belanja:
    total_belanjaan += item["harga"]

    print("Total Belanjaan : ", total_belanjaan)