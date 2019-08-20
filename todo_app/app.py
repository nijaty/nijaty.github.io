import psycopg2


connection = psycopg2.connect(
    database="db_name",
    user="db_user",
    password="baku2019",


)

cursor = connection.cursor()

print("1) Yeni mehsul elave etmek ucun 1 reqemini daxil edin\n"
      "2) Axtarish ucun 2 reqemini daxil edin\n"
      "3) Cedvelden element silmek ucun 3 reqemini daxil edin\n"
      "4) Cedveldeki elemente deyisiklik etmek ucun 4 reqemini daxil edin")
secimEt = int(input("Zehmet olmasa, secim edin: "))

if secimEt == 1:

    name = input("Mehsulun adi: ")
    quantity = input("Mehsulun miqdari: ")
    price = input("Mehsulun qiymeti: ")
    expire_date = input("Mehsulun son istifade muddeti y%-m%-d%: ")

    cursor.execute(f"INSERT INTO products (name, quantity, price, expire_date) VALUES ('{name}', '{quantity}', '{price}', '{expire_date}');")

    connection.commit()
    print("Mehsul ugurla elave olundu")
elif secimEt == 2:
    search = input("Acar soze gore axtarish etmek: ")

    cursor.execute(f"SELECT * FROM products WHERE LOWER(name) LIKE '%{search}%' OR LOWER(quantity) LIKE '%{search}%' OR LOWER(price) LIKE '%{search}%';")

    data = cursor.fetchall()

    for x in data:
        print(x)



elif secimEt == 3:


    sutunuSec = input("Silineceyi sutunu daxil edin: ")

    cergeniSec = input("Silineceyi cergeni daxil edin: ")

    cursor.execute(f"DELETE FROM products WHERE {sutunuSec}='{cergeniSec}';")

    connection.commit()

    print("Mehsul ugurla verilenler bazasindan silindi")



elif secimEt == 4:

    sutunuSec = input("Yenilenecek sutunu daxil edin: ")

    yeniElement = input("Yeni elementi daxil edin: ")


    cergeniSec = input("Yenilenecek elementi daxil edin: ")

    cursor.execute(f"UPDATE products SET {sutunuSec}='{yeniElement}' WHERE {sutunuSec}='{cergeniSec}';")

    connection.commit()

    print("Mehsul ugurla verilenler bazasinda yenilendi")



else:
    pass