

from Class_Utama import Player,Pet,Item


if __name__ == "__main__":

    print("\n========== PEMBUATAN OBJECT ==========")

    player1 = Player("P001", "Rafi", "password123")
    player2 = Player("P002", "Ahmad", "rahasia123")

   
    pet1 = Pet(
        "PET001",
        "Milo",
        "Kucing",
        "Aktif",
        80,
        100,
        120
    )

    pet2 = Pet(
        "PET002",
        "Bobby",
        "Anjing",
        "Pemalas",
        80,
        120,
        80
    )

   
    item1 = Item(
        "I001",
        "Makanan Kucing",
        5000,
        "food"
    )

    item2 = Item(
        "I002",
        "Susu",
        7000,
        "drink"
    )

    print("\n========== INSTANCE METHOD ==========")

   
    player1.list_of_pet = pet1
    player1.list_of_pet = pet2

    
    player1.tampilkan_data_user()
    pet1.tampilkan_data_pet()

    
    item1.tampilkan_info_item()
    item2.tampilkan_info_item()

   
    pet1.bermain()


    print("\n========== CLASS METHOD ==========")

    
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
    pet3.tampilkan_data_pet()

    
    print("\nTarget EXP sebelum diubah:", Pet.TARGET_EXP)
    Pet.set_target_exp(150)
    print("Target EXP setelah diubah:", Pet.TARGET_EXP)
    
    print("\n========== STATIC METHOD ==========")

    print(
        "Username 'Rafi' valid:",
        Player.validasi_username("Rafi")
    )

    print(
        "Username kosong valid:",
        Player.validasi_username("")
    )

    print(
        "Nama pet 'Milo' valid:",
        Pet.validasi_nama_pet("Milo")
    )

    print(
        "Nama pet kosong valid:",
        Pet.validasi_nama_pet("")
    )


    
    print("\n========== SETTER VALID ==========")

    player1.pet_coins = 100
    print("Pet coins:", player1.pet_coins)

    pet1.energi = 80
    print("Energi:", pet1.energi)

    pet1.mood = 90
    print("Mood:", pet1.mood)

    item1.price = 6000
    print("Harga item:", item1.price)

    item1.category = "medicine"
    print("Kategori item:", item1.category)


    print("\n========== SETTER INVALID ==========")

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