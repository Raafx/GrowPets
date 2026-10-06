from time import time

from Class_Utama import Pet

        
class Cat(Pet):
    def __init__(self, pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi):
        super().__init__(pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi)
        self.kebersihan = 100
        self.__total_grooming = 0
        
    def grooming(self):
        if(self.kebersihan == 100):
            print(f"{self.pet_name} Masih bersih! jadi ga perlu grooming ya (^_^)")
        if(self.energi < 5):
            print(f"{self.pet_name} Masih capek, ntar aja ya groomingnya (^_^)")
        else:
            
            print("Lagi Grooming.....\n")
            
            print("   /\_/\     ") 
            print("  ( -.- )~   ")  
            print("  / >👅< \  ")
            print(" /|   ||  |\ ")
            print("(_/  /\_  \_)")
            
            for i in range(35): 
                time.sleep(0.3)
                print("=", end="",flush=True)
                
            print(f"\nYey {self.pet_name} udah selesai grooming nih\n")
        
            # Efek dari method ini
            self.kebersihan = 100
            self.__energi -= 5
            self.__mood += 10
            if self.__mood > 100:
                self.__mood = 100
            self.__exp += 25
            self.__total_grooming += 1
        
        
class Dog(Pet):
    def __init__(self, pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi):
        super().__init__(pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi)
        self.loyalitas = 0
        self.__total_jalan_jalan = 0
        
    
    def jalan_jalan(self):
        if(self.__kekenyangan < 20 or self.__haus < 20 or self.__energi < 20):
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
                time.sleep(0.5)
                print("=", end="",flush=True)
                
            print(f"\nYey Kamu dan {self.pet_name} udah selesai jalan-jalannya nih\n")
            
            # Efek dari method ini
            self.loyalitas += 10
            if self.loyalitas > 100:
                self.loyalitas = 100
            self.__energi -= 20
            self.__haus -= 10
            self.__kekenyangan -= 10
            self.__mood += 20
            if self.__mood > 100:
                self.__mood = 100
            self.__exp += 35
            self.__total_jalan_jalan += 1
        
class Panda(Pet):
    def __init__(self, pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi):
        super().__init__(pet_id, pet_name, spesies, personality, max_kekenyangan, max_haus, max_energi)
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
                time.sleep(0.3)
                print("=", end="",flush=True)
                
            print(f"\nYey {self.pet_name} udah selesai meditasi nih\n")

            # Efek dari method ini
            self.ketenangan = 100
            self.__energi += 10
            self.__mood += 15
            if self.__mood > 100:
                self.__mood = 100
            self.__exp += 30
            self.__total_meditasi += 1
        
        

        
