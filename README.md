# Dokumentasi Program GrowPets (Virtual Pet Game)

Dokumen ini berisi penjelasan komprehensif mengenai program simulator hewan peliharaan virtual **GrowPets**, arsitektur class, penjelasan prinsip Pemrograman Berbasis Objek (OOP) yang diterapkan, serta panduan pengujian sistem.

## 1. Penjelasan Program

**GrowPets** adalah sebuah program virtual pet sederhana berbasis Python yang menerapkan konsep-konsep Object-Oriented Programming (OOP). Program ini dirancang untuk mensimulasikan interaksi antara pemain (*Player*), hewan peliharaan (*Pet*), dan barang/item kebutuhan (*Item*).

Melakukan aktivitas interaktif seperti bermain dengan hewan peliharaan yang akan mengubah status energi, rasa haus, kekenyangan, *mood*, dan poin pengalaman (*EXP*).

Melalui program ini, pemain dapat:

* Mengelola data akun user dan inventaris item.

* Memelihara satu atau lebih hewan peliharaan (*Pet*).

* Melakukan aktivitas interaktif seperti bermain dengan hewan peliharaan.

* Mengelola barang kebutuhan (*Item*) yang dikategorikan menjadi makanan, minuman, dan obat-obatan.

## 2. Struktur Class & Spesifikasi Code

Program ini memiliki 3 class utama yang terdefinisi di dalam berkas `Class_Utama.py`:

### A. Class `Player`

Mewakili entitas pengguna/pemain di dalam game.

* **Atribut Private (`__`)**: `__user_id`, `__password`, `__list_of_pet`, `__pet_coins`, `__inventory`.

* **Atribut Public**: `username`.

* **Property / Getter-Setter**:

  * `user_id`: Memastikan ID tidak berupa string kosong.

  * `password`: Memastikan password tidak berupa string kosong.

  * `pet_coins`: Memastikan koin bernilai non-negatif ($\ge 0$).

  * `list_of_pet`: Memastikan elemen yang ditambahkan merupakan instance dari `Pet`.

  * `inventory`: Memastikan item merupakan instance dari `Item` dan memiliki kategori valid (`food`, `drink`, atau `medicine`).

* **Method**:

  * `tampilkan_data_user()`: Menampilkan ringkasan data profil pemain.

  * `validasi_username(nama)` *(Static Method)*: Memeriksa apakah nama pengguna yang diinput valid (tidak kosong).

### B. Class `Pet`

Mewakili hewan peliharaan yang dipelihara oleh `Player`.

* **Atribut Class**: `DEFAULT_MOOD` (100), `DEFAULT_EXP` (0), `DEFAULT_FASE` (1), `TARGET_EXP` (100), `NAMA_GAME` ("GrowPets").

* **Atribut Private (`__`)**: `__pet_id`, `__kekenyangan`, `__haus`, `__energi`, `__max_kekenyangan`, `__max_haus`, `__max_energi`, `__mood`, `__exp`, `__fase`, `__total_main`, `__total_makan`, `__total_minum`, `__mengantuk`.

* **Atribut Public**: `pet_name`, `spesies`, `personality`, `penyakit`.

* **Property / Getter-Setter**:

  * `kekenyangan`, `haus`, `energi`: Memastikan nilai berada di rentang $0$ hingga batas maksimum masing-masing.

  * `mood`: Memastikan nilai $0 \le \text{mood} \le 100$.

  * `exp`: Memastikan poin pengalaman tidak bernilai negatif.

* **Method**:

  * `bermain()`: Mengurangi energi (-10), haus (-5), kekenyangan (-5) serta menambah mood (+10) dan EXP (+25). Memiliki pengecekan kondisi jika pet terlalu lelah (stat < 20).

  * `tampilkan_data_pet()`: Menampilkan seluruh kondisi dan status terkini dari pet.

  * `from_dict(data)` *(Class Method)*: *Alternative constructor* untuk membuat instance `Pet` dari tipe data dictionary.

  * `set_target_exp(target_exp)` *(Class Method)*: Mengubah variabel class `TARGET_EXP`.

  * `validasi_nama_pet(nama)` *(Static Method)*: Validasi nama pet agar tidak kosong.

### C. Class `Item`

Mewakili item/barang yang dapat dibeli atau dimiliki dalam inventaris.

* **Atribut Private (`__`)**: `__item_id`, `__price`, `__category`.

* **Atribut Public**: `name`.

* **Property / Getter-Setter**:

  * `item_id`: Memastikan ID tidak kosong.

  * `price`: Memastikan harga barang $\ge 0$.

  * `category`: Memastikan kategori barang bernilai salah satu dari `'food'`, `'drink'`, atau `'medicine'`.

* **Method**:

  * `tampilkan_info_item()`: Menampilkan atribut detail dari item.

## 3. Panduan Pengujian (Testing Guide)

Pengujian dilakukan melalui berkas `main.py` untuk menguji fungsionalitas pembuatan objek, instance method, class method, static method, serta validasi eksekusi setter (input valid vs invalid).

### Persyaratan Lingkungan

* **Python Version**: Python 3.7+

* **File Structure**:

  ```
  .
  ├── Class_Utama.py
  ├── main.py
  └── README.md
  
  ```

### Skenario Pengujian

#### 1. Inisialisasi Objek (Object Creation)

Menguji pembuatan instance dari class `Player`, `Pet`, dan `Item`.

* **Player**:

  * `player1 = Player("P001", "Rafi", "password123")`

  * `player2 = Player("P002", "Ahmad", "rahasia123")`

* **Pet**:

  * `pet1`: Milo (Kucing), Max Stats: \[Kekenyangan: 80, Haus: 100, Energi: 120\]

  * `pet2`: Bobby (Anjing), Max Stats: \[Kekenyangan: 80, Haus: 120, Energi: 80\]

* **Item**:

  * `item1`: Makanan Kucing (Harga: 5000, Kategori: "food")

  * `item2`: Susu (Harga: 7000, Kategori: "drink")

#### 2. Uji Instance Method

* Menambahkan `pet1` dan `pet2` ke dalam daftar pet milik `player1`.

* Memanggil `tampilkan_data_user()` dan `tampilkan_data_pet()`.

* Memanggil `item1.tampilkan_info_item()` dan `item2.tampilkan_info_item()`.

* Memanggil `pet1.bermain()` untuk memastikan simulasi loading bar dan perubahan statistik pet berjalan dengan benar.

#### 3. Uji Class Method

* `Pet.from_dict(...)`: Membuat instance `pet3` (Akai si Panda) dari dictionary data.

* `Pet.set_target_exp(150)`: Mengubah nilai atribut class `TARGET_EXP` global dari 100 menjadi 150.

#### 4. Uji Static Method

* `Player.validasi_username(...)`:

  * Input `"Rafi"` $\rightarrow$ **True**

  * Input `""` $\rightarrow$ **False**

* `Pet.validasi_nama_pet(...)`:

  * Input `"Milo"` $\rightarrow$ **True**

  * Input `""` $\rightarrow$ **False**

#### 5. Uji Encapsulation & Getter/Setter

##### A. Input Valid (Normal Case)

| 

| **Target Property** | **Input Value** | **Ekspektasi Output** | 
| `player1.pet_coins` | `100` | Berhasil diubah menjadi `100` | 
| `pet1.energi` | `80` | Berhasil diubah menjadi `80` | 
| `pet1.mood` | `90` | Berhasil diubah menjadi `90` | 
| `item1.price` | `6000` | Berhasil diubah menjadi `6000` | 
| `item1.category` | `"medicine"` | Berhasil diubah menjadi `"medicine"` | 

##### B. Input Invalid (Boundary & Exception Case)

| **Target Property** | **Input Value** | **Pesan Peringatan / Handling yang Diharapkan** | 
| `player1.user_id` | `""` | `"ID user tidak boleh kosong!"` | 
| `player1.password` | `""` | `"Password tidak boleh kosong!"` | 
| `player1.pet_coins` | `-100` | `"Jumlah koin tidak boleh negatif!"` | 
| `pet1.energi` | `-10` | `"Jumlah energi tidak boleh negatif atau melebihi maksimum!"` | 
| `pet1.energi` | `150` | `"Jumlah energi tidak boleh negatif atau melebihi maksimum!"` | 
| `pet1.mood` | `-10` | `"Jumlah mood tidak boleh negatif atau melebihi maksimum!"` | 
| `pet1.mood` | `150` | `"Jumlah mood tidak boleh negatif atau melebihi maksimum!"` | 
| `item1.item_id` | `""` | `"ID item tidak boleh kosong!"` | 
| `item1.price` | `-5000` | `"Harga tidak boleh negatif!"` | 
| `item1.category` | `"senjata"` | `"Kategori tidak valid! Harus 'food', 'drink', atau 'medicine'."` | 

## 4. Cara Menjalankan Pengujian

Buka terminal/command prompt, pastikan berada di direktori project yang sesuai, lalu jalankan perintah berikut:

```
python main.py

```

Jika program berjalan tanpa error dan menampilkan log validasi sesuai dengan pengujian di atas, maka implementasi class dan enkapsulasi telah berhasil berfungsi dengan baik.