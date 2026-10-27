# GrowPets

GrowPets adalah program berbasis Python bertema simulasi perawatan hewan peliharaan. Pemain dapat mengelola pet dan inventaris item, sedangkan `Shop` menyediakan fitur pembelian item. Program menerapkan konsep Object-Oriented Programming (OOP), seperti abstraksi, pewarisan, dan polimorfisme.

## Class Diagram

![Class Diagram GrowPets](docs/diagram.png)

### Penjelasan Relasi

#### 1. Asosiasi (Association)

- **`Pet` — `Disease`**: kelas `Pet` memiliki atribut `penyakit` yang dapat merujuk pada objek `Disease`. Method `cek_penyakit()` menggunakan informasi penyakit, seperti nama dan deskripsi.
- **`Shop` — `Player`**: method `beli_item(player, item, jumlah)` menerima objek `Player` sebagai parameter, lalu berinteraksi dengan saldo koin dan inventaris pemain.

#### 2. Agregasi (Aggregation)

- **`Player` ◇— `Pet`**: `Player` menyimpan daftar pet melalui atribut `__list_of_pet`.
- **`Player` ◇— `Item`**: `Player` menyimpan item pada atribut `__inventory`, yang dikelompokkan menjadi makanan, minuman, dan obat.
- **`Shop` ◇— `Item`**: `Shop` menyimpan daftar item yang tersedia untuk dibeli melalui atribut `__daftar_item`.

Agregasi menggambarkan hubungan “memiliki”, tetapi objek yang dimiliki tidak harus bergantung sepenuhnya pada objek pemiliknya.

#### 3. Komposisi (Composition)

Pada diagram, **`Shop` ◆— `Transaksi`** ditandai sebagai komposisi berdasarkan rancangan kelas. Namun, pada implementasi saat ini, objek `Transaksi` dibuat sebagai variabel lokal di dalam method `beli_item()` dan tidak disimpan sebagai atribut `Shop`. Karena itu, hubungan komposisi tersebut belum ditegakkan secara kuat oleh struktur kode; jika diagram harus sepenuhnya mencerminkan implementasi, relasi ini dapat dijelaskan sebagai penggunaan/dependensi `Shop` terhadap `Transaksi`.

## Penerapan Abstraksi

- **`Pet`** merupakan abstract class yang mewarisi `ABC`.
- Method **`makan()`**, **`minum()`**, dan **`tampilkan_info()`** pada `Pet` dideklarasikan sebagai abstract method. Kelas turunan seperti `Cat`, `Dog`, dan `Panda` perlu menyediakan implementasi method abstract tersebut.
- **`Item`** juga merupakan abstract class. Kelas turunannya, yaitu `Food`, `Drink`, dan `Medicine`, menyediakan perilaku yang lebih spesifik untuk item.

Abstract class digunakan untuk menetapkan kerangka perilaku bagi kelas turunannya dan tidak dapat diinstansiasi secara langsung selama masih memiliki abstract method yang belum diimplementasikan.

## Penerapan Polimorfisme

- **`Cat`**, **`Dog`**, dan **`Panda`** merupakan kelas turunan `Pet` yang memiliki implementasi perilaku pet masing-masing. Ketiganya dapat menyediakan implementasi method dengan nama yang sama, seperti `tampilkan_info()`, `makan()`, dan `minum()`, sesuai perilaku kelasnya.
- **`Food`**, **`Drink`**, dan **`Medicine`** merupakan kelas turunan `Item` yang dapat mengimplementasikan **`tampilkan_info_item()`** sesuai jenis itemnya, sebagaimana ditunjukkan pada diagram.

Dengan polimorfisme, method yang dipanggil dapat memiliki perilaku berbeda bergantung pada kelas objek yang digunakan.

## Screenshot Output Program




<!-- Ganti path di bawah ini setelah screenshot ditambahkan. -->
![Output utama program](screenshots/ss1.png)
![Output utama program](screenshots/ss2.png)
![Output utama program](screenshots/ss3.png)
![Output utama program](screenshots/ss4.png)
![Output utama program](screenshots/ss5.png)
![Output utama program](screenshots/ss6.png)
![Output utama program](screenshots/ss7.png)
![Output utama program](screenshots/ss8.png)
![Output utama program](screenshots/ss9.png)


