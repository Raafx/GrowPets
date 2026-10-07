from Class_Utama import Item

class Food(Item):
    def __init__(self, item_id, name, price, category, pengurangan_lapar, penambahan_energi, peningkatan_mood):
        super().__init__(item_id, name, price, category)
        self.pengurangan_lapar = pengurangan_lapar
        self.penambahan_energi = penambahan_energi
        self.peningkatan_mood = peningkatan_mood
    
    def tampilkan_info_item(self):
        print("============ Info Item =============")
        print(f"ID Item                : {self.item_id}")
        print(f"Nama Item              : {self.name}")
        print(f"Harga                  : {self.price}")
        print(f"Kategori               : {self.category}")
        print(f"Efek Pengurangan Lapar : {self.pengurangan_lapar}")
        print(f"Efek Penambahan Energi : {self.penambahan_energi}")
        print(f"Efek Peningkatan Mood  : {self.peningkatan_mood}")
        print("====================================")


class Drink(Item):
    def __init__(self, item_id, name, price, category, pengurangan_haus):
        super().__init__(item_id, name, price, category)
        self.pengurangan_haus = pengurangan_haus

    def tampilkan_info_item(self):
        print("============ Info Item =============")
        print(f"ID Item                : {self.item_id}")
        print(f"Nama Item              : {self.name}")
        print(f"Harga                  : {self.price}")
        print(f"Kategori               : {self.category}")
        print(f"Efek Pengurangan Haus  : {self.pengurangan_haus}")
        print("====================================")
        
class Medicine(Item):
    def __init__(self, item_id, name, price, category, penambahan_energi, peningkatan_mood, target_penyakit):
        super().__init__(item_id, name, price, category)
        self.penambahan_energi = penambahan_energi
        self.peningkatan_mood = peningkatan_mood
        self.target_id_penyakit = target_penyakit

    def tampilkan_info_item(self):
        print("============ Info Item =============")
        print(f"ID Item                : {self.item_id}")
        print(f"Nama Item              : {self.name}")
        print(f"Harga                  : {self.price}")
        print(f"Kategori               : {self.category}")
        print(f"Efek Penambahan Energi : {self.penambahan_energi}")
        print(f"Efek Peningkatan Mood  : {self.peningkatan_mood}")
        print(f"Target Penyakit        : {self.target_id_penyakit}")
        print("====================================")