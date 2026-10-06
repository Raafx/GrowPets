import time

class Player:
    def __init__(self, user_id, username, password):
        self.__user_id = user_id
        self.username = username
        self.__password = password
        self.__list_of_pet = []
        self.__pet_coins = 0
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
        print("Daftar Pet   :")
        for pet in self.__list_of_pet:
            print(f"- {pet.pet_name} ({pet.spesies})")
        print("====================================")
        
    @staticmethod
    def validasi_username(nama):
        if nama.strip() == "":
            return False
        return True
            
   

class Pet:
    DEFAULT_MOOD = 100
    DEFAULT_EXP = 0
    DEFAULT_FASE = 1
    TARGET_EXP = 100 
    NAMA_GAME = "GrowPets"
    
    def __init__(self, pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi):
        self.__pet_id = pet_id
        self.pet_name = pet_name
        self.spesies = spesies
        self.personality = personality
        self.__kekenyangan = max_kekenyangan  
        self.__haus = max_haus 
        self.__energi = max_energi 
        self.__max_kekenyangan = max_kekenyangan  
        self.__max_haus = max_haus 
        self.__max_energi = max_energi 
        self.__mood = Pet.DEFAULT_MOOD
        self.__exp = Pet.DEFAULT_EXP
        self.__fase = Pet.DEFAULT_FASE
        self.penyakit = None 
        self.__total_main = 0
        self.__total_makan = 0
        self.__total_minum = 0
        self.__mengantuk = False 
        
    @classmethod 
    def from_dict(cls, data): 
        return cls(data["pet_id"], 
                   data["pet_name"], 
                   data["spesies"], 
                   data["personality"], 
                   data["max_kekenyangan"], 
                   data["max_haus"], 
                   data["max_energi"] )
        
    @staticmethod
    def validasi_nama_pet(nama):
        if nama.strip() == "":
            return False
        return True

    def bermain(self):
        if(self.__kekenyangan < 20 or self.__haus < 20 or self.__energi < 20):
            print(f"{self.pet_name} lagi capek, jangan digangguin ya (^_^)")
            print(f"Isi dulu kebutuhan {self.pet_name} biar bisa main lagi!!")
        else:
            
            print("Lagi Main.....")
            print('''
 /\\_/\\
( ^.^ )
 > ^ <
                  ''')
            for i in range(35): 
                time.sleep(0.1)
                print("=", end="",flush=True)
                
            print("\nYey pet kamu udah selesai main\n")
            
            self.__energi -= 10
            self.__haus -= 5
            self.__kekenyangan -= 5
            self.__mood += 10
            if self.__mood > 100:
                self.__mood = 100
            self.__exp += 25
            self.__total_main += 1
            
    def tampilkan_data_pet(self):
        print("============ Data Pet =============")
        print(f"Nama Pet   : {self.pet_name}")
        print(f"Spesies    : {self.spesies}")
        print(f"Personality: {self.personality}")
        print(f"Kekenyangan: {self.__kekenyangan}/{self.__max_kekenyangan}")
        print(f"Haus       : {self.__haus}/{self.__max_haus}")
        print(f"Energi     : {self.__energi}/{self.__max_energi}")
        print(f"Mood       : {self.__mood}/100")
        print(f"Exp        : {self.__exp}/{Pet.TARGET_EXP}")
        print(f"Fase       : {self.__fase}")
        if self.penyakit:
            print(f"Penyakit   : {self.penyakit}")
        else:
            print("Penyakit   : Tidak ada")
        print("===================================")
        
    @classmethod
    def set_target_exp(cls, target_exp):
        cls.TARGET_EXP = target_exp
        
    @property
    def kekenyangan(self):
        return self.__kekenyangan
    
    @kekenyangan.setter
    def kekenyangan(self, jumlah):
        if jumlah < 0 or jumlah > self.__max_kekenyangan:
            print("Jumlah kekenyangan tidak boleh negatif atau melebihi maksimum!")
        else:
            self.__kekenyangan = jumlah
    
    @property
    def haus(self):
        return self.__haus 
    
    @haus.setter
    def haus(self, jumlah):
        if jumlah < 0 or jumlah > self.__max_haus  :
            print("Jumlah haus tidak boleh negatif atau melebihi maksimum!")
        else:
            self.__haus = jumlah
            
    @property
    def energi(self):
        return self.__energi
    
    @energi.setter
    def energi(self, jumlah):
        if jumlah < 0 or jumlah > self.__max_energi:
            print("Jumlah energi tidak boleh negatif atau melebihi maksimum!")
        else:
            self.__energi = jumlah
    
    @property
    def mood(self):
        return self.__mood  
    
    @mood.setter
    def mood(self, jumlah):
        if jumlah < 0 or jumlah > 100:
            print("Jumlah mood tidak boleh negatif atau melebihi maksimum!")
        else:
            self.__mood = jumlah
    
    @property
    def exp(self):
        return self.__exp
    
    @exp.setter
    def exp(self, jumlah):
        if jumlah < 0:
            print("Jumlah exp tidak boleh negatif!")
        else:
            self.__exp = jumlah

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
        

        
