import sqlite3
import time

conn = sqlite3.connect('buku.db')
conn2 = sqlite3.connect(':memory:')

cursor = conn.cursor()
cursor2 = conn2.cursor()

cursor2.execute("""CREATE TABLE IF NOT EXISTS keranjang (
        id_keranjang INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        judul_buku TEXT NOT NULL,
        jumlah_pembelian INTEGER NOT NULL,
        harga_buku INTEGER NOT NULL,
        tanggal_beli TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    )""")

def showAllData():
    #Show all data info
    cursor.execute("SELECT * FROM buku")
    result = cursor.fetchall()
    for i in result:
        print(i)

    conn.commit()

    print("\n")

def searchBook():
    #search book by name
    name = input("Nama buku: ")
    query = f'SELECT * FROM buku WHERE judul_buku="{name}"'
    cursor.execute(query)
    result = cursor.fetchone()

    if (result == None):
        print("Hasil pencarian tidak ada")
    else:
        print(result)

    print("\n")

def addCart():
    #add books to the cart
    hasil = 0
    total = 0
    tambah = int(input("Masukkan id buku: "))
    jumlah = int(input("Masukkan jumlah pembelian: "))
    ambil = f'SELECT judul_buku FROM buku WHERE id_buku={tambah}'
    cursor.execute(ambil)
    result = cursor.fetchone()
    for row in result:
        hasil = row

    ambil_harga = f'SELECT harga_buku FROM buku WHERE id_buku={tambah}'
    cursor.execute(ambil_harga)
    harga = cursor.fetchone()
    for row in harga:
        total = row

    query = f'INSERT INTO keranjang(judul_buku, jumlah_pembelian, harga_buku) VALUES ("{hasil}", {jumlah}, {total * jumlah})'
    cursor2.execute(query)

    conn2.commit()

    print("\n")

def showCart():
    # Show all books in cart
    cursor2.execute("SELECT * FROM keranjang")
    result = cursor2.fetchall()
    for i in result:
        print(i)

    conn2.commit()

    print("\n")

def deleteCart():
    # delete books in cart
    keranjangId = int(input('Id keranjang: '))
    query = f'DELETE FROM keranjang WHERE id_keranjang={keranjangId}'
    cursor2.execute(query)

    conn2.commit()

    print("\n")

def buy():
    #execution
    cursor2.execute("SELECT judul_buku, jumlah_pembelian, harga_buku FROM keranjang")
    Data = cursor2.fetchall()
    formatted_row = '{:<20} {:<15} {:12}'
    t = time.localtime()

    print("-------------------------------------------------")
    print("\t\t\tTOKO BERNICHA SEJAHTERA\n")
    print("Kasir : Bernicha elek")
    print("Waktu : %s " % time.asctime(t))
    print("-------------------------------------------------")
    print(formatted_row.format("Judul", "Jumlah Pembelian", "\t\tHarga"))
    print("-------------------------------------------------")
    for Row in Data:
        print(formatted_row.format(*Row))

    conn2.commit()

    harga = f'SELECT SUM(harga_buku) FROM keranjang'
    cursor2.execute(harga)
    total = cursor2.fetchone()

    print("-------------------------------------------------")
    print("\nTotal harga: ")
    for row in total:
        print(row)

    print("\n")

    print("-------------------------------------------------")
    print("\t\t\tTerima kasih telah berbelanja")
    print("-------------------------------------------------")

    cursor2.execute("DELETE FROM keranjang")

while True:
    print("Pilihan Menu Pengguna")
    print("""
            1. Show All Book
            2. Search Book
            3. Add Cart
            4. Show Cart
            5. Delete Cart
            6. Buy
            7. Exit

        """)
    pilihan = int(input('Pilihan: '))

    if (pilihan == 1):
        showAllData()
    elif (pilihan == 2):
        searchBook()
    elif (pilihan == 3):
        addCart()
    elif (pilihan == 4):
        showCart()
    elif (pilihan == 5):
        deleteCart()
    elif (pilihan == 6):
        buy()
    elif (pilihan == 7):
        break
    else:
        print('Menu tidak valid!')