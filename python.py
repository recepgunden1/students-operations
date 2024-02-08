import sqlite3 as sql

con = sql.connect("veritabani.db")
print("Bağlantı gerçekleştirildi..")

cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS OGRENCILER (
                Isim TEXT,
                Soyisim TEXT,
                Numara INTEGER,
                Sinif TEXT
)""")

def veri_ekle():
    isim = input("Öğrencinin ismi: ")
    soyisim = input("Öğrencinin soyismi: ")
    numara = int(input("Öğrencinin numarası: "))
    sinif = input("Öğrencinin sınıfı: ")
    cursor.execute("INSERT INTO OGRENCILER VALUES (?,?,?,?)", (isim, soyisim, numara, sinif))
    print("Veriler database'e eklendi..")
    con.commit()

def veri_listele():
    cursor.execute("SELECT * FROM OGRENCILER")
    veriler = cursor.fetchall()

    if not veriler:
        print("Veritabanında henüz öğrenci bilgisi bulunmamaktadır.")
    else:
        for veri in veriler:
            print("İsim:", veri[0])
            print("Soyisim:", veri[1])
            print("Numara:", veri[2])
            print("Sınıf:", veri[3])
            print("-" * 20)

def veri_sil():
    numara = int(input("Silmek istediğiniz öğrencinin numarasını girin: "))
    cursor.execute("DELETE FROM OGRENCILER WHERE Numara=?", (numara,))
    print("Öğrenci bilgisi silindi.")
    con.commit()

print("""
*************************************
öğrenci veri işlemlerine hoş geldiniz
1 - Öğrenci ekle 
2 - Öğrencileri listele
3 - Öğrenci sil
4 - ÇIKIŞ
*************************************
""")

while True:
    islem = input("İşleminizi giriniz: ")
    if islem == "1":
        veri_ekle()
    elif islem == "2":
        veri_listele()
    elif islem == "3":
        veri_sil()
    elif islem == "4":
        break

con.close()
