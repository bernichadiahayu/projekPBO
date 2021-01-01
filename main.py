import sqlite3

conn = sqlite3.connect('buku.db')

cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS buku (
        id_buku INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nama_pengarang TEXT NOT NULL,
        judul_buku TEXT NOT NULL,
        tebal_buku INTEGER NOT NULL,
        harga_buku INTEGER NOT NULL,
        tanggal_terbit TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    )""")

conn.commit()

def insertBooks():
    # insert new books
    judul = input('Judul Buku: ')
    nama_pengarang = input('Nama pengarang: ')
    harga = int(input('Harga Buku: '))
    tebal = int(input('Tebal Buku: '))
    query = f'INSERT INTO buku(judul_buku, nama_pengarang, harga_buku, tebal_buku) VALUES ("{judul}", "{nama_pengarang}", {harga}, {tebal})'
    cursor.execute(query)

    conn.commit()

    print("\n")

def showData():
    # show information about selected book
    bukuId = int(input('Id buku: '))
    query = f'SELECT * FROM buku WHERE id_buku={bukuId}'
    cursor.execute(query)
    print(cursor.fetchone())

    conn.commit()

    print("\n")

def showAllData():
    #Show all data info
    cursor.execute("SELECT * FROM buku")
    result = cursor.fetchall()
    for i in result:
        print(i)

    conn.commit()

    print("\n")

def changeInfo():
    # change information on selected book
    bukuId = int(input('Id buku: '))
    change = input('Yang ingin dirubah: ')
    value = input('Data yang akan dirubah: ')

    if (isinstance(value, str) == True):
        query = f'UPDATE buku SET "{change}"="{value}" WHERE id_buku={bukuId}'
    else:
        query = f'UPDATE buku SET "{change}"={value} WHERE id_buku={bukuId}'
    cursor.execute(query)

    conn.commit()

    print("\n")

def delete():
    # delete book
    bukuId = int(input('Id buku: '))
    query = f'DELETE FROM buku WHERE id_buku={bukuId}'
    cursor.execute(query)

    conn.commit()

    print("\n")

while True:
    print("Pilihan Menu")
    print("""
        1. Insert Book
        2. Show Data by Id
        3. Show All Data
        4. Change Info by Id
        5. Delete Data
        6. Exit
        
    """)
    pilihan = int(input('Pilihan: '))

    if (pilihan == 1):
        insertBooks()
    elif (pilihan == 2):
        showData()
    elif (pilihan == 3):
        showAllData()
    elif (pilihan == 4):
        changeInfo()
    elif (pilihan == 5):
        delete()
    elif (pilihan == 6):
        break
    else:
        print('Menu tidak valid!')

conn.close()