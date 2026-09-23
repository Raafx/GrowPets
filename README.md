# GrowPets — Dokumentasi Program OOP Python

## 1. Deskripsi Program

**GrowPets** adalah program simulasi sederhana berbasis CLI (Command Line Interface) yang menerapkan konsep **Object-Oriented Programming (OOP)** menggunakan Python.

Program ini mensimulasikan pengguna yang memiliki hewan peliharaan (*pet*), item, koin, dan beberapa status pet seperti kekenyangan, haus, energi, mood, serta EXP.

Program dibuat dengan tiga class utama:

- `Player` — merepresentasikan pengguna/pemain.
- `Pet` — merepresentasikan hewan peliharaan.
- `Item` — merepresentasikan item yang dapat dimiliki pemain.

Program dibagi menjadi dua bagian:

- `Class_Utama.py` → berisi definisi class `Player`, `Pet`, dan `Item`.
- File utama/testing → melakukan pembuatan object dan pengujian berbagai fitur OOP.

---

## 2. Struktur Program

Struktur sederhananya:

```text
GrowPets/
├── Class_Utama.py
└── Main.py
```

> Nama file utama dapat disesuaikan dengan nama file yang digunakan. Pada kode pengujian, class diimpor menggunakan:
>
> `from Class_Utama import Player, Pet, Item`

---

# 3. Penjelasan Class

## 3.1 Class `Player`

Class `Player` digunakan untuk menyimpan data pemain.

### Atribut instance

| Atribut | Keterangan |
|---|---|
| `__user_id` | ID unik pemain |
| `username` | Nama pengguna |
| `__password` | Password pengguna |
| `__list_of_pet` | Daftar pet yang dimiliki |
| `__pet_coins` | Jumlah koin pemain |
| `__inventory` | Inventory yang terdiri dari food, drink, dan medicine |

Atribut yang diawali `__` merupakan **private attribute**, sehingga aksesnya dilakukan melalui method/property yang disediakan.

### Property dan Setter

#### `user_id`
Digunakan untuk mengambil dan mengubah ID pemain.

Setter menolak ID berupa string kosong.

#### `password`
Digunakan untuk mengambil dan mengubah password.

Setter menolak password kosong.

#### `pet_coins`
Digunakan untuk mengambil dan mengubah jumlah koin.

Setter menolak jumlah koin negatif.

#### `list_of_pet`
Digunakan untuk menambahkan object `Pet` ke daftar pet pemain.

Setter melakukan validasi menggunakan:

```python
isinstance(pet, Pet)
```

Dengan demikian, hanya object dari class `Pet` yang dapat dimasukkan.

#### `inventory`
Digunakan untuk menambahkan object `Item` ke inventory.

Item akan dimasukkan berdasarkan kategorinya:

- `food`
- `drink`
- `medicine`

Setter juga memvalidasi agar hanya object `Item` yang dapat dimasukkan.

### Instance Method

#### `tampilkan_data_user()`

Menampilkan informasi pemain, jumlah koin, dan daftar pet yang dimiliki.

### Static Method

#### `validasi_username(nama)`

Digunakan untuk mengecek apakah username kosong atau tidak.

Method ini menggunakan `@staticmethod` karena tidak membutuhkan data dari object `Player`.

---

# 4. Class `Pet`

Class `Pet` digunakan untuk merepresentasikan hewan peliharaan dalam game.

## Class Attribute

Class `Pet` memiliki beberapa atribut yang digunakan bersama oleh seluruh object:

| Class Attribute | Nilai Awal | Keterangan |
|---|---:|---|
| `DEFAULT_MOOD` | `100` | Mood awal pet |
| `DEFAULT_EXP` | `0` | EXP awal pet |
| `DEFAULT_FASE` | `1` | Fase awal pet |
| `TARGET_EXP` | `100` | Target EXP |
| `NAMA_GAME` | `"GrowPets"` | Nama game |

Karena merupakan **class attribute**, nilainya berada pada level class dan dapat diakses menggunakan `Pet.NAMA_GAME`, `Pet.TARGET_EXP`, dan sebagainya.

## Atribut instance

Setiap object `Pet` memiliki data masing-masing, seperti:

- `__pet_id`
- `pet_name`
- `spesies`
- `personality`
- `__kekenyangan`
- `__haus`
- `__energi`
- `__max_kekenyangan`
- `__max_haus`
- `__max_energi`
- `__mood`
- `__exp`
- `__fase`
- `penyakit`
- `__total_main`
- `__total_makan`
- `__total_minum`
- `__mengantuk`

## Class Method

### `from_dict(cls, data)`

Method ini digunakan untuk membuat object `Pet` berdasarkan data dalam dictionary.

Contoh:

```python
data_pet = {
    "pet_id": "PET003",
    "pet_name": "Akai",
    "spesies": "Panda",
    "personality": "Ceria",
    "max_kekenyangan": 80,
    "max_haus": 80,
    "max_energi": 100
}

pet3 = Pet.from_dict(data_pet)
```

Method ini merupakan **class method** karena menggunakan `cls` dan membuat object dari class tersebut.

### `set_target_exp(cls, target_exp)`

Digunakan untuk mengubah class attribute `TARGET_EXP`.

Contoh:

```python
Pet.set_target_exp(150)
```

Setelah method dijalankan, nilai:

```python
Pet.TARGET_EXP
```

menjadi `150`.

## Instance Method

### `bermain()`

Method ini digunakan untuk mensimulasikan pet bermain.

Jika salah satu kebutuhan pet kurang dari 20, pet tidak dapat bermain.

Jika kondisi mencukupi:

1. Menampilkan animasi bermain.
2. Energi berkurang 10.
3. Haus berkurang 5.
4. Kekenyangan berkurang 5.
5. Mood bertambah 10, maksimal 100.
6. EXP bertambah 25.
7. Jumlah bermain bertambah 1.

Program juga menggunakan:

```python
time.sleep(0.1)
```

dan:

```python
flush=True
```

agar animasi loading ditampilkan secara bertahap di terminal.

### `tampilkan_data_pet()`

Menampilkan informasi lengkap pet, termasuk status kebutuhan, mood, EXP, fase, dan penyakit.

## Static Method

### `validasi_nama_pet(nama)`

Digunakan untuk mengecek apakah nama pet kosong atau tidak.

Method ini tidak membutuhkan data object `Pet`, sehingga menggunakan `@staticmethod`.

## Property dan Setter

Class `Pet` memiliki property:

- `kekenyangan`
- `haus`
- `energi`
- `mood`
- `exp`

Setter melakukan validasi agar nilai tidak keluar dari batas yang telah ditentukan.

Contoh:

```python
pet1.energi = 80
```

adalah data valid.

Sedangkan:

```python
pet1.energi = -10
```

atau:

```python
pet1.energi = 150
```

ditolak apabila melebihi batas maksimum energi pet.

---

# 5. Class `Item`

Class `Item` digunakan untuk merepresentasikan item dalam game.

## Atribut

| Atribut | Keterangan |
|---|---|
| `__item_id` | ID item |
| `name` | Nama item |
| `__price` | Harga item |
| `__category` | Kategori item |

## Property dan Setter

### `item_id`

Setter menolak ID item kosong.

### `price`

Setter menolak harga negatif.

### `category`

Setter hanya menerima tiga kategori:

```text
food
drink
medicine
```

Jika kategori lain diberikan, data akan ditolak.

### Instance Method

#### `tampilkan_info_item()`

Menampilkan ID, nama, harga, dan kategori item.

---

# 6. Konsep OOP yang Diterapkan

Program ini menerapkan beberapa konsep OOP berikut.

## 6.1 Class dan Object

Class digunakan sebagai blueprint, sedangkan object merupakan instance dari class.

Contoh:

```python
player1 = Player("P001", "Rafi", "password123")
pet1 = Pet("PET001", "Milo", "Kucing", "Aktif", 80, 100, 120)
item1 = Item("I001", "Makanan Kucing", 5000, "food")
```

## 6.2 Encapsulation

Beberapa atribut dibuat private menggunakan awalan `__`, misalnya:

```python
self.__password
self.__pet_coins
self.__energi
self.__price
```

Akses terhadap data tersebut dilakukan melalui property dan setter.

## 6.3 Getter dan Setter

Getter digunakan untuk mengambil nilai:

```python
print(pet1.energi)
```

Setter digunakan untuk mengubah nilai sekaligus melakukan validasi:

```python
pet1.energi = 80
```

## 6.4 Instance Method

Instance method menggunakan `self` dan bekerja terhadap object tertentu.

Contoh:

```python
pet1.bermain()
```

## 6.5 Class Method

Class method menggunakan `@classmethod` dan menerima parameter `cls`.

Contoh:

```python
Pet.from_dict(data_pet)
Pet.set_target_exp(150)
```

## 6.6 Static Method

Static method tidak menggunakan `self` maupun `cls`.

Contoh:

```python
Player.validasi_username("Rafi")
Pet.validasi_nama_pet("Milo")
```

Method tersebut hanya melakukan proses validasi yang tidak bergantung pada data object tertentu.

## 6.7 Validasi Data

Setter digunakan untuk mencegah data yang tidak valid masuk ke object.

Contohnya:

- koin tidak boleh negatif;
- energi tidak boleh negatif atau melebihi maksimum;
- mood harus berada pada rentang 0–100;
- harga tidak boleh negatif;
- kategori item harus sesuai pilihan yang tersedia.

---

# 7. Panduan Menjalankan Program

Pastikan Python sudah terinstall.

Buka terminal pada folder project, kemudian jalankan file utama:

```bash
python Main.py
```

Jika nama file utama berbeda, sesuaikan dengan nama file tersebut.

Pastikan `Class_Utama.py` berada di folder yang sama dengan file utama karena program menggunakan:

```python
from Class_Utama import Player, Pet, Item
```

---

# 8. Panduan Pengujian

Bagian testing pada program dibagi menjadi beberapa tahap.

## 8.1 Pengujian Pembuatan Object

Program membuat minimal dua object dari setiap class:

### Player

```python
player1 = Player("P001", "Rafi", "password123")
player2 = Player("P002", "Ahmad", "rahasia123")
```

### Pet

```python
pet1 = Pet(...)
pet2 = Pet(...)
```

### Item

```python
item1 = Item(...)
item2 = Item(...)
```

Tujuannya untuk menunjukkan bahwa satu class dapat digunakan untuk membuat beberapa object dengan data yang berbeda.

---

## 8.2 Pengujian Instance Method

Program menjalankan:

```python
player1.tampilkan_data_user()
pet1.tampilkan_data_pet()
item1.tampilkan_info_item()
item2.tampilkan_info_item()
pet1.bermain()
```

Perhatikan perubahan status `pet1` setelah menjalankan `bermain()`.

Energi, haus, dan kekenyangan akan berkurang, sedangkan mood dan EXP akan bertambah.

---

## 8.3 Pengujian Class Method

Program menguji:

```python
pet3 = Pet.from_dict(data_pet)
```

Kemudian mengubah target EXP:

```python
print("Target EXP sebelum diubah:", Pet.TARGET_EXP)
Pet.set_target_exp(150)
print("Target EXP setelah diubah:", Pet.TARGET_EXP)
```

Output menunjukkan perubahan nilai `TARGET_EXP` dari `100` menjadi `150`.

---

## 8.4 Pengujian Static Method

Username valid:

```python
Player.validasi_username("Rafi")
```

Hasil:

```text
True
```

Username kosong:

```python
Player.validasi_username("")
```

Hasil:

```text
False
```

Hal yang sama dilakukan pada validasi nama pet.

---

## 8.5 Pengujian Setter Valid

Contoh data valid:

```python
player1.pet_coins = 100
pet1.energi = 80
pet1.mood = 90
item1.price = 6000
item1.category = "medicine"
```

Program kemudian menampilkan nilai yang berhasil disimpan.

---

## 8.6 Pengujian Setter Tidak Valid

Program juga memasukkan beberapa data yang tidak valid:

```python
player1.user_id = ""
player1.password = ""
player1.pet_coins = -100

pet1.energi = -10
pet1.energi = 150

pet1.mood = -10
pet1.mood = 150

item1.item_id = ""
item1.price = -5000
item1.category = "senjata"
```

Program seharusnya menampilkan pesan error tanpa mengganti nilai sebelumnya.

Contoh:

```text
Jumlah koin tidak boleh negatif!
Jumlah energi tidak boleh negatif atau melebihi maksimum!
Harga tidak boleh negatif!
Kategori tidak valid! Harus 'food', 'drink', atau 'medicine'.
```

---

# 9. Ringkasan Pengujian

| Fitur | Pengujian | Hasil yang Diharapkan |
|---|---|---|
| Object `Player` | Membuat `player1` dan `player2` | Object berhasil dibuat |
| Object `Pet` | Membuat `pet1` dan `pet2` | Object berhasil dibuat |
| Object `Item` | Membuat `item1` dan `item2` | Object berhasil dibuat |
| Instance method | `bermain()` | Status pet berubah |
| Instance method | Method tampil data | Data ditampilkan |
| Class method | `from_dict()` | Object `Pet` berhasil dibuat dari dictionary |
| Class method | `set_target_exp()` | `TARGET_EXP` berubah |
| Static method | Validasi username | Menghasilkan `True`/`False` |
| Static method | Validasi nama pet | Menghasilkan `True`/`False` |
| Setter valid | Nilai dalam batas | Nilai diterima |
| Setter invalid | Nilai di luar batas | Nilai ditolak dan pesan error ditampilkan |

---

# 10. Kesimpulan

Program **GrowPets** merupakan implementasi sederhana OOP menggunakan Python dengan tiga class utama, yaitu `Player`, `Pet`, dan `Item`.

Program telah menerapkan:

- class dan object;
- instance attribute;
- class attribute;
- private attribute;
- instance method;
- class method;
- static method;
- getter menggunakan `@property`;
- setter menggunakan `@property.setter`;
- validasi data pada setter;
- pembuatan object dari dictionary;
- pengujian data valid dan tidak valid.

Dengan struktur tersebut, program tidak hanya menjalankan simulasi pet sederhana, tetapi juga menunjukkan penerapan beberapa konsep dasar OOP Python dalam satu program.
