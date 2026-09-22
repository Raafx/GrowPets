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
    def pet_coins(self):
        return self.__pet_coins
    
    @pet_coins.setter
    def pet_coins(self,jumlah):
        if jumlah < 0:
            print("Jumlah koin tidak boleh negatif!")
        else:
            self.__pet_coins = jumlah
            
    @property
    def pet_coins(self):
        return self.__pet_coins
    
    @pet_coins.setter
    def pet_coins(self,jumlah):
        if jumlah < 0:
            print("Jumlah koin tidak boleh negatif!")
        else:
            self.__pet_coins = jumlah
    
    def tampilkan_data_user(self):
        print("============ Data User =============")
        print(f"Username    : {self.username}")
        print(f"Jumlah Koin : {self.__pet_coins}")
        print("Daftar Pet   :")
        for pet in self.__list_of_pet:
            print(f"- {pet.pet_name} ({pet.spesies})")
        print("====================================")
            
   

class Pet:
    DEFAULT_MOOD = 100
    DEFAULT_EXP = 0
    DEFAULT_FASE = 1
    TARGET_EXP = 100 
    
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
        self.personality = personality
        self.penyakit = None #berisi instance dari Disease
        self.total_main = 0
        self.total_makan = 0
        self.total_minum = 0
        self.mengantuk = False 
        
    
    def bermain(self):
        if(self.__kekenyangan < 20 or self.__haus < 20 or self.__energi < 20):
            print(f"{self.pet_name} lagi capek, jangan digangguin ya (^_^)")
            print(f"Isi dulu kebutuhan {self.pet_name} biar bisa main lagi!!")
        else:
            
            print("Lagi Main.....")
            for i in range(20): #instance dari Food
                print("=", end="")
                time.sleep(0.5)
            
            self.__energi -= 10
            self.__haus -= 5
            self.__kekenyangan -= 5
            self.__mood += 10
            if self.__mood > 100:
                self.__mood = 100
            self.__exp += 25
            self.total_main += 1
        

class Item:
    def __init__(self, item_id, name, price, category):
        self.__item_id = item_id
        self.name = name
        self.__price = price
        self.__category = category
        

        
