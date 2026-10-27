import time

from Class_Utama import Pet

        
class Cat(Pet):
    def __init__(self, pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan):
        super().__init__(pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan)
        self.kebersihan = 100
        self.__total_grooming = 0
        
    def grooming(self):
        if(self.kebersihan == 100):
            print(f"{self.pet_name} Masih bersih! jadi ga perlu grooming ya (^_^)")
            return
        if(self._energi < 5):
            print(f"{self.pet_name} Masih capek, ntar aja ya groomingnya (^_^)")
            return
        else:
            
            print("Lagi Grooming.....\n")
            
            print("   /\_/\     ") 
            print("  ( -.- )~   ")  
            print("  / >👅< \  ")
            print(" /|   ||  |\ ")
            print("(_/  /\_  \_)")
            
            for i in range(35): 
                time.sleep(0.1)
                print("=", end="",flush=True)
                
            print(f"\nYey {self.pet_name} udah selesai grooming nih\n")
        
            # Efek dari method ini
            self.kebersihan = 100
            self._energi -= 5
            self._mood += 10
            if self._mood > 100:
                self._mood = 100
            self._exp += 25
            self.__total_grooming += 1
            
        
    def makan(self, food):
        from Class_Turunan_Item import Food
        
        if(self.kekenyangan == self._max_kekenyangan):
            print(f"{self.pet_name} masih kenyang nih, ntar aja yak makannya (^_^)\n")
            return
        
        if isinstance(food, Food):
            if food.name in self._list_makanan:
                
                print(" /\_/\      ") 
                print("( o.o )  🥣")
                print(" / >🍚     ")
                
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

                self._exp += 10
                if self._exp >= Pet.TARGET_EXP:
                    self._exp = 0
                    self._fase += 1
                    print(f"\n{self.pet_name} udah naik ke fase {self._fase} nih!!\n")
                    
                self.kebersihan -= 5
                if self.kebersihan < 0:
                    self.kebersihan = 0
                    
                self._total_makan += 1
                
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
            if self._haus >= self._max_haus:
                self._haus = self._max_haus
                
            self._exp += 5
            if self._exp >= Pet.TARGET_EXP:
                self._exp = 0
                self._fase += 1
                print(f"\n{self.pet_name} udah naik ke fase {self._fase} nih!!\n")
                
            self.kebersihan -= 2
            if self.kebersihan < 0:
                self.kebersihan = 0
            
            
            self._total_minum += 1
            
            print(f"\nYey {self.pet_name} udah selesai minum nih (˵>ᗜ<˵) !!\n")
                
        else:
            print("Ini bukan minuman oiii ヽ(#`Д´)ﾉ")
        
    
    def tampilkan_info(self):
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
        print(f"Kebersihan : {self.kebersihan}/100")
        if self.penyakit:
            print(f"Penyakit   : {self.penyakit}")
        else:
            print("Penyakit   : Tidak ada")
        print("===================================")
        
        
        
        
class Dog(Pet):
    def __init__(self, pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan):
        super().__init__(pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan)
        self.loyalitas = 0
        self.__total_jalan_jalan = 0
        
    
    def jalan_jalan(self):
        if(self._kekenyangan < 20 or self._haus < 20 or self._energi < 20):
            print(f"{self.pet_name} lagi capek, jangan digangguin ya (^_^)")
            print(f"Isi dulu kebutuhan {self.pet_name} biar bisa main lagi!!")
        else:
            
            print("Lagi Jalan-Jalan.....\n")    
               
            print("  (o o)                   ")
            print("  /| |\____               ")
            print(" / | |     \    / \__     ")
            print("  /   \     \__(    @\___ ")
            print(" /     \       /         O")
            print("              /   /----/  ")
            print("             (_/ (_/      ")
            
            for i in range(35): 
                time.sleep(0.1)
                print("=", end="",flush=True)
                
            print(f"\nYey Kamu dan {self.pet_name} udah selesai jalan-jalannya nih\n")
            
            # Efek dari method ini
            self.loyalitas += 10
            if self.loyalitas > 100:
                self.loyalitas = 100
            self._energi -= 20
            self._haus -= 10
            self._kekenyangan -= 10
            self._mood += 20
            if self._mood > 100:
                self._mood = 100
            self._exp += 35
            self.__total_jalan_jalan += 1
            
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

                self._exp += 10
                if self._exp >= Pet.TARGET_EXP:
                    self._exp = 0
                    self._fase += 1
                    print(f"\n{self.pet_name} udah naik ke fase {self._fase} nih!!\n")

            
                self.loyalitas += 10
                if self.loyalitas > 100:
                    self.loyalitas = 100
                    
                self._total_makan += 1
                
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
            if self._haus >= self._max_haus:
                self._haus = self._max_haus
                
            self._exp += 5
            if self._exp >= Pet.TARGET_EXP:
                self._exp = 0
                self._fase += 1
                print(f"\n{self.pet_name} udah naik ke fase {self._fase} nih!!\n")
                
            self.loyalitas += 5
            if self.loyalitas > 100:
                self.loyalitas = 100
            
            self._total_minum += 1
            
            print(f"\nYey {self.pet_name} udah selesai minum nih (˵>ᗜ<˵) !!\n")
                
        else:
            print("Ini bukan minuman oiii ヽ(#`Д´)ﾉ")
    
            
    def tampilkan_info(self):
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
        print(f"Loyalitas  : {self.loyalitas}/100")
        if self.penyakit:
            print(f"Penyakit   : {self.penyakit}")
        else:
            print("Penyakit   : Tidak ada")
        print("===================================")
        
        
class Panda(Pet):
    def __init__(self, pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan):
        super().__init__(pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi, list_makanan)
        self.ketenangan = 100
        self.__total_meditasi = 0
        
    def meditasi(self):
        if(self.ketenangan == 100):
            print(f"{self.pet_name} lagi tenang banget nih! jadi ga perlu meditasi ya (^_^)")
        else:
            
            print("Lagi Meditasi.....\n")
            print("  (o)_(o)  ")
            print("  ( -.- )  ") 
            print(" /| === |\ ")
            print("(_|_____|_)")
            print("  (_____)  ")
            
            for i in range(35): 
                time.sleep(0.1)
                print("=", end="",flush=True)
                
            print(f"\nYey {self.pet_name} udah selesai meditasi nih\n")

            # Efek dari method ini
            self.ketenangan = 100
            self._energi += 10
            self._mood += 15
            if self._mood > 100:
                self._mood = 100
            self._exp += 30
            self.__total_meditasi += 1
    
        
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

                self._exp += 10
                if self._exp >= Pet.TARGET_EXP:
                    self._exp = 0
                    self._fase += 1
                    print(f"\n{self.pet_name} udah naik ke fase {self._fase} nih!!\n")

                
                self.ketenangan += 5
                if self.ketenangan > 100:
                    self.ketenangan = 100
                    
                self._total_makan += 1
                
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
            if self._haus >= self._max_haus:
                self._haus = self._max_haus
                
            self._exp += 5
            if self._exp >= Pet.TARGET_EXP:
                self._exp = 0
                self._fase += 1
                print(f"\n{self.pet_name} udah naik ke fase {self._fase} nih!!\n")
                
            self.ketenangan += 5
            if self.ketenangan > 100:
                self.ketenangan = 100
                
            self._total_minum += 1
            
            print(f"\nYey {self.pet_name} udah selesai minum nih (˵>ᗜ<˵) !!\n")
                
        else:
            print("Ini bukan minuman oiii ヽ(#`Д´)ﾉ")
            
    def tampilkan_info(self):
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
        print(f"Ketenangan : {self.ketenangan}/100")
        if self.penyakit:
            print(f"Penyakit   : {self.penyakit}")
        else:
            print("Penyakit   : Tidak ada")
        print("===================================")
        
        
        
        
        

        
