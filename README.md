# GrowPets — Posttest 2

## 1. Deskripsi Program

**GrowPets** adalah program simulasi hewan peliharaan berbasis **CLI (Command Line Interface)** yang dibuat menggunakan Python dan menerapkan konsep **Object-Oriented Programming (OOP)**.

Pada versi **Posttest 2**, program dikembangkan dari versi sebelumnya dengan menambahkan:

- inheritance / pewarisan class;
- class turunan untuk berbagai jenis pet;
- class turunan untuk berbagai jenis item;
- method overriding;
- validasi menggunakan `isinstance()`;
- hubungan antar-object berupa **agregasi, asosiasi, dan komposisi**;
- sistem Shop untuk membeli item;
- object `Transaksi` yang dibuat saat proses pembelian.

Pet memiliki beberapa status seperti:

- kekenyangan;
- haus;
- energi;
- mood;
- EXP;
- fase;
- penyakit.

Jenis pet yang tersedia:

- `Cat`
- `Dog`
- `Panda`

Jenis item yang tersedia:

- `Food`
- `Drink`
- `Medicine`

---

# 2. Struktur Folder

Struktur folder `posttest2`:

```text
posttest2/
├── Class_Utama.py
├── Class_Turunan_Pet.py
├── Class_Turunan_Item.py
└── main.py
```

### `Class_Utama.py`

Berisi class utama:

- `Player`
- `Pet`
- `Item`
- `Disease`
- `Shop`
- `Transaksi`

### `Class_Turunan_Pet.py`

Berisi class turunan dari `Pet`:

- `Cat`
- `Dog`
- `Panda`

### `Class_Turunan_Item.py`

Berisi class turunan dari `Item`:

- `Food`
- `Drink`
- `Medicine`

### `main.py`

Digunakan untuk membuat object dan menjalankan pengujian program.

---

# 3. Struktur Pewarisan Class

Struktur inheritance pada program:

```text
                 Pet
              /   |   \
            Cat  Dog  Panda


                 Item
               /  |  \
            Food Drink Medicine
```

`Cat`, `Dog`, dan `Panda` mewarisi atribut dan method dari `Pet`.

Sedangkan `Food`, `Drink`, dan `Medicine` mewarisi atribut dan method dari `Item`.

Contoh:

```python
class Cat(Pet):
    ...
```

dan:

```python
class Food(Item):
    ...
```

Constructor class turunan memanggil constructor parent menggunakan:

```python
super().__init__(...)
```

---

# 4. Class `Player`

`Player` merepresentasikan pengguna yang memainkan game.

## Atribut

| Atribut | Keterangan |
|---|---|
| `__user_id` | ID user |
| `username` | Nama pengguna |
| `__password` | Password pengguna |
| `__list_of_pet` | Daftar pet yang dimiliki |
| `__pet_coins` | Jumlah Pet Coins |
| `__inventory` | Inventory berdasarkan kategori item |

Inventory terdiri dari:

```python
{
    "food": [],
    "drink": [],
    "medicine": []
}
```

## Method

### `tampilkan_data_user()`

Menampilkan informasi user, Pet Coins, pet yang dimiliki, dan item dalam inventory.

### `validasi_username(nama)`

Merupakan **static method** yang digunakan untuk memvalidasi apakah username kosong.

Contoh:

```python
Player.validasi_username("Raafx")
```

### `tambah_item(item)`

Menambahkan object item ke inventory berdasarkan tipe item:

- `Food` → `food`
- `Drink` → `drink`
- `Medicine` → `medicine`

Method menggunakan `isinstance()` untuk menentukan tipe object.

### `tambah_pet(pet)`

Menambahkan object pet ke daftar pet berdasarkan jenis pet:

- `Cat`
- `Dog`
- `Panda`

### `buat_pet(...)`

Membuat object pet secara langsung di dalam method `Player`.

Spesies menentukan class yang dibuat:

```text
cat   → Cat
dog   → Dog
panda → Panda
```

Setelah object dibuat, object tersebut dimasukkan ke daftar pet menggunakan `tambah_pet()`.

Contoh:

```python
player.buat_pet(
    "C001",
    "Oyen",
    "Cat",
    "Active",
    100,
    100,
    100,
    ["Ikan", "Ayam", "Whiskas"]
)
```

---

# 5. Class `Pet`

`Pet` merupakan class dasar untuk semua jenis hewan peliharaan.

## Class Attribute

```python
DEFAULT_MOOD = 100
DEFAULT_EXP = 0
DEFAULT_FASE = 1
TARGET_EXP = 100
NAMA_GAME = "GrowPets"
```

Class attribute digunakan sebagai nilai yang dapat digunakan bersama oleh object dalam class tersebut.

## Atribut Instance

Beberapa atribut yang dimiliki setiap pet:

| Atribut | Keterangan |
|---|---|
| `__pet_id` | ID pet |
| `pet_name` | Nama pet |
| `spesies` | Jenis/spesies pet |
| `personality` | Kepribadian pet |
| `_kekenyangan` | Status kekenyangan |
| `_haus` | Status haus |
| `_energi` | Status energi |
| `_max_kekenyangan` | Nilai maksimum kekenyangan |
| `_max_haus` | Nilai maksimum haus |
| `_max_energi` | Nilai maksimum energi |
| `_mood` | Mood pet |
| `_exp` | EXP pet |
| `_fase` | Fase pet |
| `penyakit` | Penyakit yang dimiliki pet |
| `__total_makan` | Jumlah pet makan |
| `__total_minum` | Jumlah pet minum |
| `_mengantuk` | Status mengantuk |
| `_list_makanan` | Daftar makanan yang dapat dimakan |

## Class Method

### `from_dict(cls, data)`

Membuat object `Pet` berdasarkan dictionary.

Contoh bentuk data:

```python
data_pet = {
    "pet_id": "P001",
    "pet_name": "Milo",
    "spesies": "Cat",
    "personality": "Active",
    "max_kekenyangan": 100,
    "max_haus": 100,
    "max_energi": 100,
    "list_makanan": ["Ikan", "Ayam"]
}

pet = Pet.from_dict(data_pet)
```

### `set_target_exp(cls, target_exp)`

Mengubah nilai class attribute `TARGET_EXP`.

Contoh:

```python
Pet.set_target_exp(150)
```

## Static Method

### `validasi_nama_pet(nama)`

Memeriksa apakah nama pet kosong.

Contoh:

```python
Pet.validasi_nama_pet("Oyen")
```

menghasilkan:

```text
True
```

## Instance Method

### `tampilkan_data_pet()`

Menampilkan data pet, termasuk:

- nama;
- spesies;
- personality;
- kekenyangan;
- haus;
- energi;
- mood;
- EXP;
- fase;
- penyakit.

### `makan(food)`

Membuat pet memakan object `Food`.

Method melakukan pengecekan:

1. Pet tidak boleh sudah kenyang.
2. Object yang diberikan harus merupakan `Food`.
3. Nama makanan harus terdapat dalam `_list_makanan`.

Jika berhasil, status pet dapat berubah berdasarkan efek makanan:

- kekenyangan bertambah;
- energi bertambah;
- mood bertambah;
- jumlah makan bertambah.

### `minum(drink)`

Membuat pet meminum object `Drink`.

Object yang diberikan harus merupakan instance dari `Drink`.

---

# 6. Class `Cat`

`Cat` merupakan subclass dari `Pet`.

Selain atribut yang diwarisi dari `Pet`, `Cat` memiliki:

```python
kebersihan
__total_grooming
```

## `grooming()`

Digunakan untuk melakukan grooming pada kucing.

Jika kebersihan sudah `100`, grooming tidak dilakukan.

Jika energi kurang dari `5`, grooming juga tidak dilakukan.

Jika grooming berhasil:

- kebersihan menjadi `100`;
- energi berkurang `5`;
- mood bertambah `10`;
- EXP bertambah `25`;
- jumlah grooming bertambah.

---

# 7. Class `Dog`

`Dog` merupakan subclass dari `Pet`.

Atribut tambahan:

```python
loyalitas
__total_jalan_jalan
```

## `jalan_jalan()`

Digunakan untuk mengajak anjing jalan-jalan.

Pet harus memiliki kondisi yang mencukupi untuk melakukan aktivitas.

Jika berhasil:

- loyalitas bertambah `10`, maksimal `100`;
- energi berkurang `20`;
- haus berkurang `10`;
- kekenyangan berkurang `10`;
- mood bertambah `20`, maksimal `100`;
- EXP bertambah `35`;
- jumlah jalan-jalan bertambah.

---

# 8. Class `Panda`

`Panda` merupakan subclass dari `Pet`.

Atribut tambahan:

```python
ketenangan
__total_meditasi
```

## `meditasi()`

Digunakan untuk melakukan meditasi.

Jika `ketenangan == 100`, meditasi tidak diperlukan.

Jika meditasi dilakukan:

- ketenangan menjadi `100`;
- energi bertambah `10`;
- mood bertambah `15`, maksimal `100`;
- EXP bertambah `30`;
- jumlah meditasi bertambah.

---

# 9. Class `Item`

`Item` merupakan class dasar untuk berbagai item yang digunakan dalam game.

## Atribut

| Atribut | Keterangan |
|---|---|
| `__item_id` | ID item |
| `name` | Nama item |
| `__price` | Harga item |
| `__category` | Kategori item |

Kategori yang digunakan:

```text
food
drink
medicine
```

## `tampilkan_info_item()`

Menampilkan informasi dasar item.

Method ini kemudian dioverride oleh class `Food`, `Drink`, dan `Medicine`.

---

# 10. Class `Food`

`Food` merupakan subclass dari `Item`.

Atribut tambahan:

```python
pengurangan_lapar
penambahan_energi
peningkatan_mood
```

## `tampilkan_info_item()`

Method ini melakukan **method overriding** terhadap method dengan nama yang sama pada `Item`.

Informasi yang ditampilkan meliputi:

- ID;
- nama;
- harga;
- kategori;
- efek pengurangan lapar;
- efek penambahan energi;
- efek peningkatan mood.

---

# 11. Class `Drink`

`Drink` merupakan subclass dari `Item`.

Atribut tambahan:

```python
pengurangan_haus
```

## `tampilkan_info_item()`

Method ini melakukan overriding dan menampilkan:

- ID;
- nama;
- harga;
- kategori;
- efek pengurangan haus.

---

# 12. Class `Medicine`

`Medicine` merupakan subclass dari `Item`.

Atribut tambahan:

```python
penambahan_energi
peningkatan_mood
target_penyakit
```

Pada implementasi class, target penyakit disimpan sebagai:

```python
target_id_penyakit
```

## `tampilkan_info_item()`

Method ini melakukan overriding dan menampilkan:

- ID;
- nama;
- harga;
- kategori;
- efek penambahan energi;
- efek peningkatan mood;
- target penyakit.

---

# 13. Class `Disease`

`Disease` digunakan untuk merepresentasikan penyakit yang dapat dimiliki pet.

## Atribut

| Atribut | Keterangan |
|---|---|
| `__disease_id` | ID penyakit |
| `name` | Nama penyakit |
| `deskripsi` | Deskripsi penyakit |

## `tampilkan_info_penyakit()`

Menampilkan informasi penyakit.

Contoh:

```python
penyakit1 = Disease(
    "P001",
    "Flu",
    "Penyakit yang menyebabkan demam dan batuk"
)

penyakit1.tampilkan_info_penyakit()
```

Pada `posttest2` saat ini, object `Disease` baru digunakan untuk menampilkan informasi dan belum dihubungkan dengan mekanisme pengobatan pet.

---

# 14. Class `Shop`

`Shop` digunakan sebagai tempat penyimpanan item yang dapat dibeli oleh player.

## Atribut

Shop memiliki daftar item berdasarkan kategori:

```python
{
    "food": [],
    "drink": [],
    "medicine": []
}
```

## `tambah_item_ke_shop(item)`

Menambahkan object `Item` ke daftar item Shop berdasarkan kategorinya.

Method memvalidasi object menggunakan:

```python
isinstance(item, Item)
```

## `beli_item(player, item, jumlah)`

Digunakan untuk membeli item.

Parameter:

- `player` → object `Player` yang melakukan pembelian;
- `item` → object item yang ingin dibeli;
- `jumlah` → jumlah item yang dibeli.

Alur pembelian:

```text
Player memilih item
        ↓
Shop mengecek item
        ↓
Menghitung total harga
        ↓
Mengecek Pet Coins
        ↓
Pet Coins dikurangi
        ↓
Item dimasukkan ke inventory Player
        ↓
Object Transaksi dibuat
        ↓
Informasi transaksi ditampilkan
```

Pembelian hanya berhasil apabila Pet Coins player mencukupi.

---

# 15. Class `Transaksi`

`Transaksi` merupakan class yang digunakan untuk menyimpan detail pembelian.

Atribut:

| Atribut | Keterangan |
|---|---|
| `item_dibeli` | Object item yang dibeli |
| `harga_item` | Harga satu item |
| `jumlah_dibeli` | Jumlah item |
| `total_harga` | Total harga pembelian |

## `tampilkan_info_transaksi()`

Menampilkan:

- item yang dibeli;
- harga item;
- jumlah;
- total harga.

Object `Transaksi` dibuat di dalam method `Shop.beli_item()` ketika pembelian berhasil.

---

# 16. Konsep OOP yang Diterapkan

## 16.1 Class dan Object

Class digunakan sebagai blueprint untuk membuat object.

Contoh:

```python
player = Player("P001", "Raafx", "r1234")
```

```python
ikan = Food(
    "F001",
    "Ikan",
    10000,
    "food",
    20,
    15,
    10
)
```

---

## 16.2 Encapsulation

Program menggunakan atribut private dengan awalan `__`.

Contoh:

```python
self.__password
self.__pet_coins
self.__pet_id
self.__price
```

Akses terhadap beberapa atribut dilakukan melalui property.

---

## 16.3 Inheritance

Class turunan memperoleh atribut dan method dari class induknya.

Contoh:

```python
class Cat(Pet):
```

dan:

```python
class Food(Item):
```

---

## 16.4 `super()`

Constructor class turunan memanggil constructor class induk menggunakan:

```python
super().__init__(...)
```

Hal ini membuat atribut dasar dari `Pet` atau `Item` tetap dapat digunakan oleh class turunannya.

---

## 16.5 Method Overriding

Class `Food`, `Drink`, dan `Medicine` memiliki method:

```python
tampilkan_info_item()
```

yang menggantikan implementasi method dengan nama sama pada class `Item`.

Dengan demikian, masing-masing jenis item dapat menampilkan informasi khusus sesuai atributnya.

---

## 16.6 Polymorphism melalui `isinstance()`

Program menggunakan `isinstance()` untuk mengenali tipe object.

Contoh pada `Player.tambah_item()`:

```python
if isinstance(item, Food):
    ...
elif isinstance(item, Drink):
    ...
elif isinstance(item, Medicine):
    ...
```

Hal serupa digunakan untuk mengenali jenis pet.

---

## 16.7 Property, Getter, dan Setter

Beberapa atribut memiliki property dan setter untuk mengatur akses sekaligus melakukan validasi.

Contoh:

```python
pet.energi
```

dan:

```python
pet.energi = 80
```

Setter digunakan untuk memastikan nilai berada pada batas yang ditentukan.

---

## 16.8 Static Method

Contoh:

```python
Player.validasi_username("Raafx")
```

dan:

```python
Pet.validasi_nama_pet("Oyen")
```

Method tersebut tidak bergantung pada data object tertentu.

---

## 16.9 Class Method

Contoh:

```python
Pet.from_dict(data)
```

dan:

```python
Pet.set_target_exp(150)
```

Class method menggunakan `cls` untuk bekerja pada level class.

---

# 17. Relasi Antar-Class

Program `posttest2` menerapkan beberapa jenis hubungan antar-object.

## 17.1 Agregasi — Player dan Pet

Player memiliki daftar pet:

```python
self.__list_of_pet = []
```

Pet dibuat kemudian dimasukkan ke daftar milik Player.

Pada `main.py`:

```python
player.buat_pet(...)
```

Object pet kemudian disimpan pada:

```python
player.list_of_pet
```

Pet dapat dianggap sebagai object yang berada di dalam kumpulan Player.

---

## 17.2 Agregasi — Shop dan Item

Shop memiliki daftar item:

```python
self.__daftar_item = {
    "food": [],
    "drink": [],
    "medicine": []
}
```

Item dibuat di luar Shop, kemudian dimasukkan menggunakan:

```python
shop.tambah_item_ke_shop(item)
```

Contoh:

```python
shop.tambah_item_ke_shop(ikan)
shop.tambah_item_ke_shop(ayam)
shop.tambah_item_ke_shop(air)
```

---

## 17.3 Asosiasi — Shop dan Player

Method:

```python
shop.beli_item(player, item, jumlah)
```

menerima object `Player` sebagai parameter.

Artinya Shop berinteraksi dengan Player ketika proses pembelian berlangsung.

---

## 17.4 Asosiasi — Pet dan Item

Pet berinteraksi dengan item ketika menjalankan:

```python
oyen.makan(ikan)
```

atau:

```python
oyen.minum(air)
```

Object item diberikan sebagai parameter kepada method Pet.

---

## 17.5 Komposisi — Shop dan Transaksi

Pada saat pembelian berhasil, object `Transaksi` dibuat di dalam method:

```python
Shop.beli_item()
```

Contohnya:

```python
transaksi = Transaksi(
    item,
    item.price,
    jumlah,
    total_harga
)
```

Object `Transaksi` hanya dibuat sebagai bagian dari proses pembelian dan tidak disimpan sebagai bagian permanen dari Shop.

---

# 18. Alur Program `main.py`

Secara umum, pengujian pada `main.py` berjalan seperti berikut:

```text
Membuat Player
      ↓
Membuat Pet melalui Player.buat_pet()
      ↓
Mengambil object Cat, Dog, dan Panda
      ↓
Menjalankan method khusus masing-masing pet
      ↓
Membuat object Food dan Drink
      ↓
Membuat object Shop
      ↓
Menambahkan item ke Shop
      ↓
Mengisi Pet Coins
      ↓
Membeli item
      ↓
Item masuk ke inventory Player
      ↓
Pet menggunakan item
      ↓
Menampilkan informasi item
      ↓
Membuat object Disease
      ↓
Menampilkan informasi penyakit
```

---

# 19. Contoh Penggunaan

## Membuat Player

```python
player = Player("P001", "Raafx", "r1234")
```

## Membuat Pet melalui Player

```python
player.buat_pet(
    "C001",
    "Oyen",
    "Cat",
    "Active",
    100,
    100,
    100,
    ["Ikan", "Ayam", "Whiskas"]
)
```

## Mengambil Pet

```python
oyen = player.list_of_pet[0]
```

## Menjalankan aktivitas khusus

```python
oyen.kebersihan = 50
oyen.grooming()
```

## Membuat Item

```python
ikan = Food(
    "F001",
    "Ikan",
    10000,
    "food",
    20,
    15,
    10
)
```

## Membuat Shop

```python
shop = Shop()
shop.tambah_item_ke_shop(ikan)
```

## Membeli Item

```python
player.pet_coins = 100000
shop.beli_item(player, ikan, 2)
```

## Menggunakan Item

```python
oyen.kekenyangan = 50
oyen.makan(ikan)
```

---

# 20. Cara Menjalankan Program

Masuk ke folder `posttest2`:

```bash
cd posttest2
```

Kemudian jalankan:

```bash
python main.py
```

Pastikan ketiga file module berada pada folder yang sama:

```text
Class_Utama.py
Class_Turunan_Pet.py
Class_Turunan_Item.py
main.py
```

Program menggunakan import antar-file seperti:

```python
from Class_Utama import Pet
```

dan:

```python
from Class_Turunan_Item import Drink, Food
```

---

# 21. Catatan Implementasi Posttest 2

Versi `posttest2` saat ini berfokus pada penerapan konsep OOP dan hubungan antar-class.

Beberapa fitur sudah tersedia tetapi belum digunakan secara penuh dalam gameplay, misalnya:

- `Medicine` sudah dibuat sebagai subclass `Item`, tetapi belum digunakan pada proses pengobatan pet.
- `Disease` sudah dapat dibuat dan ditampilkan, tetapi belum dihubungkan dengan sistem penyakit pet.
- atribut penghitung seperti `__total_grooming`, `__total_jalan_jalan`, dan `__total_meditasi` masih disimpan secara internal dan belum memiliki method tampilan khusus.
- `main.py` berfungsi sebagai program pengujian/demo, bukan loop gameplay interaktif penuh.

---

# 22. Ringkasan Konsep OOP

| Konsep | Implementasi |
|---|---|
| Class & Object | `Player`, `Pet`, `Item`, `Cat`, `Dog`, `Panda`, dll. |
| Encapsulation | Atribut private dengan `__` |
| Property | `user_id`, `password`, `pet_coins`, `kekenyangan`, `haus`, `energi`, `mood`, `exp`, dll. |
| Inheritance | `Cat/Dog/Panda → Pet`, `Food/Drink/Medicine → Item` |
| `super()` | Constructor class turunan |
| Method Overriding | `tampilkan_info_item()` pada subclass Item |
| Static Method | `validasi_username()`, `validasi_nama_pet()` |
| Class Method | `from_dict()`, `set_target_exp()` |
| Polymorphism / Type Dispatch | `isinstance()` |
| Aggregation | `Player → Pet`, `Shop → Item` |
| Association | `Shop ↔ Player`, `Pet ↔ Item` |
| Composition | `Shop → Transaksi` |

---

## 23. Penutup

`GrowPets Posttest 2` merupakan pengembangan program simulasi pet yang digunakan untuk menerapkan berbagai konsep dasar hingga menengah dalam **Object-Oriented Programming menggunakan Python**.

Program tidak hanya menggunakan class dan object, tetapi juga menunjukkan bagaimana beberapa object dapat saling berinteraksi melalui inheritance, overriding, validasi tipe, property, serta hubungan agregasi, asosiasi, dan komposisi.
