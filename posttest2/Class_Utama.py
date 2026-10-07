import time

class Player:
    def __init__(self, user_id, username, password):
        self.__user_id = user_id
        self.username = username
        self.__password = password
        self.__list_of_pet = []
        self.__pet_coins = 100
        self.__inventory = {"food":[],
                            "drink":[],
                            "medicine":[]}
        
    @property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self, user_id):
        if user_id.strip() == "":
            print("ID user tidak boleh kosong!")
        else:
            self.__user_id = user_id
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, new_password):
        if new_password.strip() == "":
            print("Password tidak boleh kosong!")
        else:
            self.__password = new_password
        
    @property
    def pet_coins(self):
        return self.__pet_coins
    
    @pet_coins.setter
    def pet_coins(self,jumlah):
        if jumlah < 0:
            print("Jumlah koin tidak boleh negatif!")
        else:
            self.__pet_coins = jumlah
            
    @property
    def list_of_pet(self):
        return self.__list_of_pet
    
    @list_of_pet.setter
    def list_of_pet(self, pet):
        if isinstance(pet, Pet):
            self.__list_of_pet.append(pet)
        else:
            print("Hanya objek Pet yang dapat ditambahkan ke daftar pet.")
            
    @property
    def inventory(self):
        return self.__inventory
    
    @inventory.setter
    def inventory(self, item):
        if isinstance(item, Item):
            if item.category in self.__inventory:
                self.__inventory[item.category].append(item)
            else:
                print("Kategori item tidak valid.")
        else:
            print("Hanya objek Item yang dapat ditambahkan ke inventory.")
    
    def tampilkan_data_user(self):
        print("============ Data User =============")
        print(f"Username    : {self.username}")
        print(f"Jumlah Koin : {self.__pet_coins}")
        print(f"Daftar Pet  :")
        for pet in self.__list_of_pet:
            print(f"- {pet.pet_name} ({pet.spesies})")
        print(f"Daftar Item :")
        for item_type, items in self.inventory.items():
            for item in items:
                print(f"- {item_type}: {item.item_name}")
        print("====================================")
        
    @staticmethod
    def validasi_username(nama):
        if nama.strip() == "":
            return False
        return True
    
    def tambah_item(self, item):
        from Class_Turunan_Item import Food,Medicine,Drink
        
        if isinstance(item,Item):
            if isinstance(item, Food) :
                self.__inventory["food"].append(item)
                
            elif isinstance(item, Drink):
                self.__inventory["drink"].append(item)
                
            elif isinstance(item, Medicine):
                self.__inventory["medicine"].append(item)
                
            else:
                print("Item tidak dikenali!")
        else:
            print("Objek bukan item!")
            
    
            
    def tambah_pet(self, pet):
        from Class_Turunan_Pet import Cat,Dog,Panda
        
        if isinstance(pet,Pet):
            if isinstance(pet, Cat):
                self.__list_of_pet.append(pet)
                
            elif isinstance(pet, Dog):
                self.__list_of_pet.append(pet)
                
            elif isinstance(pet, Panda):
                self.__list_of_pet.append(pet)
                
            else:
                print("Pet tidak dikenali!")
        else:
            print("Objek bukan pet!")
            
    def buat_pet(self, pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan):
        from Class_Turunan_Pet import Cat, Dog, Panda
        
        if spesies.lower() == "cat":
            new_pet = Cat(pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan)
            self.tambah_pet(new_pet)
            print(f"Pet baru {pet_name} (Kucing) berhasil dibuat!")
            
        elif spesies.lower() == "dog":
            new_pet = Dog(pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan)
            self.tambah_pet(new_pet)
            print(f"Pet baru {pet_name} (Anjing) berhasil dibuat!")
            
        elif spesies.lower() == "panda":
            new_pet = Panda(pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan)
            self.tambah_pet(new_pet)
            print(f"Pet baru {pet_name} (Panda) berhasil dibuat!")
            
        else:
            print("Spesies tidak valid! Pilih antara 'Cat', 'Dog', atau 'Panda'.")
            
            
   

class Pet:
    DEFAULT_MOOD = 100
    DEFAULT_EXP = 0
    DEFAULT_FASE = 1
    TARGET_EXP = 100 
    NAMA_GAME = "GrowPets"
    
    def __init__(self, pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan):
        self.__pet_id = pet_id
        self.pet_name = pet_name
        self.spesies = spesies
        self.personality = personality
        self._kekenyangan = max_kekenyangan  
        self._haus = max_haus 
        self._energi = max_energi 
        self._max_kekenyangan = max_kekenyangan  
        self._max_haus = max_haus 
        self._max_energi = max_energi 
        self._max_mood = Pet.DEFAULT_MOOD
        self._mood = Pet.DEFAULT_MOOD
        self._exp = Pet.DEFAULT_EXP
        self._fase = Pet.DEFAULT_FASE
        self.penyakit = None 
        self.__total_makan = 0
        self.__total_minum = 0
        self._mengantuk = False 
        self._list_makanan = list_makanan #list makanan yang bisa dimakan oleh pet tersebut 
        
    @classmethod 
    def from_dict(cls, data): 
        return cls(data["pet_id"], 
                   data["pet_name"], 
                   data["spesies"], 
                   data["personality"], 
                   data["max_kekenyangan"], 
                   data["max_haus"], 
                   data["max_energi"],
                   data["list_makanan"] )
        
    @staticmethod
    def validasi_nama_pet(nama):
        if nama.strip() == "":
            return False
        return True
        
    @classmethod
    def set_target_exp(cls, target_exp):
        cls.TARGET_EXP = target_exp
        
    @property
    def kekenyangan(self):
        return self._kekenyangan
    
    @kekenyangan.setter
    def kekenyangan(self, jumlah):
        if jumlah < 0 or jumlah > self._max_kekenyangan:
            print("Jumlah kekenyangan tidak boleh negatif atau melebihi maksimum!")
        else:
            self._kekenyangan = jumlah
    
    @property
    def haus(self):
        return self._haus 
    
    @haus.setter
    def haus(self, jumlah):
        if jumlah < 0 or jumlah > self._max_haus  :
            print("Jumlah haus tidak boleh negatif atau melebihi maksimum!")
        else:
            self._haus = jumlah
            
    @property
    def energi(self):
        return self._energi
    
    @energi.setter
    def energi(self, jumlah):
        if jumlah < 0 or jumlah > self._max_energi:
            print("Jumlah energi tidak boleh negatif atau melebihi maksimum!")
        else:
            self._energi = jumlah
    
    @property
    def mood(self):
        return self._mood  
    
    @mood.setter
    def mood(self, jumlah):
        if jumlah < 0 or jumlah > 100:
            print("Jumlah mood tidak boleh negatif atau melebihi maksimum!")
        else:
            self._mood = jumlah
    
    @property
    def exp(self):
        return self._exp
    
    @exp.setter
    def exp(self, jumlah):
        if jumlah < 0:
            print("Jumlah exp tidak boleh negatif!")
        else:
            self._exp = jumlah
            
    def tampilkan_data_pet(self):
        print("============ Data Pet =============")
        print(f"Nama Pet   : {self.pet_name}")
        print(f"Spesies    : {self.spesies}")
        print(f"Personality: {self.personality}")
        print(f"Kekenyangan: {self._kekenyangan}/{self._max_kekenyangan}")
        print(f"Haus       : {self._haus}/{self._max_haus}")
        print(f"Energi     : {self._energi}/{self._max_energi}")
        print(f"Mood       : {self._mood}/100")
        print(f"Exp        : {self._exp}/{Pet.TARGET_EXP}")
        print(f"Fase       : {self._fase}")
        if self.penyakit:
            print(f"Penyakit   : {self.penyakit}")
        else:
            print("Penyakit   : Tidak ada")
        print("===================================")
        
    def makan(self, food):
        from Class_Turunan_Item import Food
        
        if(self.kekenyangan == self._max_kekenyangan):
            print(f"{self.pet_name} masih kenyang nih, ntar aja yak makannya (^_^)\n")
            return
        
        if isinstance(food, Food):
            if food.name in self._list_makanan:
                
                print(f"\n{self.pet_name} lagi makan...")
                for i in range(35): 
                    time.sleep(0.1)
                    print("=", end="",flush=True)
                    
                self._kekenyangan += food.pengurangan_lapar
                if self._kekenyangan >= self._max_kekenyangan:
                    self._kekenyangan = self._max_kekenyangan
                    
                self._energi += food.penambahan_energi
                if self._energi >= self._max_energi:
                    self._energi = self._max_energi
                    
                self._mood += food.peningkatan_mood
                if self._mood >= self._max_mood:
                    self._mood = self._max_mood
                    
                self.__total_makan += 1
                
                print(f"\nYey {self.pet_name} udah selesai makan nih (˵>ᗜ<˵) !!\n")
            else:
                print(f"{self.pet_name} ga bisa makan {food.name} nih, coba kasih makanan lain aja (^_^)\n")
                
        else:
            print("Ini bukan makanan oiii ヽ(#`Д´)ﾉ")
            
    def minum(self, drink):
        from Class_Turunan_Item import Drink
        
        if(self._haus == self._max_haus):
            print(f"{self.pet_name} masih belum haus nih, ntar aja yak minumnya (^_^)\n")
            return
        
        if isinstance(drink, Drink):
            print(f"\n{self.pet_name} lagi minum...")
            for i in range(35): 
                time.sleep(0.03)
                print("=", end="",flush=True)
                
            self._haus += drink.pengurangan_haus
            
            self.__total_minum += 1
            
            print(f"\nYey {self.pet_name} udah selesai minum nih (˵>ᗜ<˵) !!\n")
                
        else:
            print("Ini bukan minuman oiii ヽ(#`Д´)ﾉ")
                
        

class Item:
    def __init__(self, item_id, name, price, category):
        self.__item_id = item_id
        self.name = name
        self.__price = price
        self.__category = category
        
    @property
    def item_id(self):
        return self.__item_id
    
    @item_id.setter
    def item_id(self, item_id):
        if item_id.strip() == "":
            print("ID item tidak boleh kosong!")
        else:
            self.__item_id = item_id

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price < 0:
            print("Harga tidak boleh negatif!")
        else:
            self.__price = price
            
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, category):
        if category not in ["food", "drink", "medicine"]:
            print("Kategori tidak valid! Harus 'food', 'drink', atau 'medicine'.")
        else:
            self.__category = category

        
    def tampilkan_info_item(self):
        print("============ Info Item =============")
        print(f"ID Item   : {self.__item_id}")
        print(f"Nama Item : {self.name}")
        print(f"Harga     : {self.__price}")
        print(f"Kategori  : {self.__category}")
        print("====================================")
        

class Disease:
    def __init__(self, disease_id, name, deskripsi):
        self.__disease_id = disease_id
        self.name = name
        self.deskripsi = deskripsi
        
    @property
    def disease_id(self):
        return self.__disease_id
    
    @disease_id.setter
    def disease_id(self, disease_id):
        if disease_id.strip() == "":
            print("ID penyakit tidak boleh kosong!")
        else:
            self.__disease_id = disease_id
            
    def tampilkan_info_penyakit(self):
        print("============ Info Penyakit =============")
        print(f"ID Penyakit : {self.__disease_id}")
        print(f"Nama Penyakit: {self.name}")
        print(f"Deskripsi   : {self.deskripsi}")
        print("========================================")
        
        
class Shop:
    def __init__(self):
        self.__daftar_item = {"food":[],
                            "drink":[],
                            "medicine":[]}
        
    def beli_item(self, player, item, jumlah):
        
        if not isinstance(item, Item):
            print("Yang kamu beli bukan item woii!\n")
            return
        
        if item in self.__daftar_item[item.category]:
            total_harga = jumlah*item.price
            
            
            if player.pet_coins >= total_harga:
                player.pet_coins -= total_harga
                for i in range(jumlah):
                    player.tambah_item(item)
                    
                print("Pembelian berhasil! Item sudah ditambahkan ke inventory kamu (＾▽＾)\n")
                transaksi = Transaksi(item, item.price, jumlah, total_harga)
                transaksi.tampilkan_info_transaksi()
            
            else:
                print("Pembelian gagal! Pet Coins kamu masih kurang (ㅠ﹏ㅠ)")    
                
    def tambah_item_ke_shop(self, item):
        if isinstance(item, Item):
            if item.category in self.__daftar_item:
                self.__daftar_item[item.category].append(item)
            else:
                print("Kategori item tidak valid.")
        else:
            print("Hanya objek Item yang dapat ditambahkan ke shop.")    

# class bagian komposisi dari Shop                    
class Transaksi:
    def __init__(self, item_dibeli, harga_item, jumlah_dibeli ,total_harga ):
        self.item_dibeli = item_dibeli
        self.harga_item = harga_item
        self.jumlah_dibeli = jumlah_dibeli
        self.total_harga = total_harga
        
    def tampilkan_info_transaksi(self):
        print("============ Info Transaksi =============")
        print(f"Item Dibeli : {self.item_dibeli.name}")
        print(f"Harga Item  : {self.harga_item}")
        print(f"Jumlah      : {self.jumlah_dibeli}")
        print(f"Total Harga : {self.total_harga}")
        print("=========================================")
                    
          
                 
            
        
