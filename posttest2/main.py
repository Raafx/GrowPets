from Class_Utama import Disease, Player,Pet,Item, Shop
from Class_Turunan_Item import Drink, Food


if __name__ == "__main__":

    player = Player("P001","Raafx","r1234")
    
    print(player.tampilkan_data_user())
    
    # Agregasi: Buat pet baru dan masukin ke list_of_pet milik player
    player.buat_pet("C001","Oyen","Cat","Active",100,100,100, ["Ikan", "Ayam", "Whiskas"])
    player.buat_pet("D001","Oggy","Dog","Lazy",120,100,80, ["Daging", "Sosis", "Pedigree"])
    player.buat_pet("P001","Pooh","Panda","Lazy",150,120,100, ["Bamboo", "Buah", "Sayuran"])
    
    print(player.tampilkan_data_user())
    
    # akses class yang diturunkan dari class utama
    oyen = player.list_of_pet[0]
    oggy = player.list_of_pet[1]
    pooh = player.list_of_pet[2]
    
    # tampilkan data pet
    print(oyen.tampilkan_data_pet())
    print(oggy.tampilkan_data_pet())
    print(pooh.tampilkan_data_pet())
    
    # spesial method dari masing-masing class turunan pet
    oyen.kebersihan = 50
    pooh.ketenangan = 50
    oyen.grooming()
    oggy.jalan_jalan()
    pooh.meditasi()
    
    
    # buat objek item makanan
    ikan = Food("F001","Ikan",10000,"food",20,15,10)
    ayam = Food("F002","Ayam",15000,"food",20,10,10)
    daging = Food("F003","Daging",20000,"food",25,10,5)
    bamboo = Food("F004","Bamboo",12000,"food",10,5,10)
    
    # buat objek item minuman
    air = Drink("D001","Air",5000,"drink",20)
    susu = Drink("D002","Susu",10000,"drink",25)
    jus = Drink("D003","Jus",15000,"drink",30)
    
    # Asosiasi: item sebagai parameter ke shop
    # Agregasi: buat objek shop dan masukin item ke list_of_item milik shop 
    shop = Shop()
    shop.tambah_item_ke_shop(ikan)
    shop.tambah_item_ke_shop(ayam)
    shop.tambah_item_ke_shop(daging)
    shop.tambah_item_ke_shop(bamboo)
    shop.tambah_item_ke_shop(air)
    shop.tambah_item_ke_shop(susu)
    shop.tambah_item_ke_shop(jus)
    
    # atur pet coins ke 100000 biar bisa beli item
    player.pet_coins = 100000
    
    # Asosiasi: beli item dari shop, menggunakan objek player dan itemsebagai parameter
    shop.beli_item(player, ikan, 2)
    shop.beli_item(player, ayam, 1)
    shop.beli_item(player, daging, 3)

    # atur kekenyangan pet ke 50 biar bisa makan
    oyen.kekenyangan = 50
    oggy.kekenyangan = 50
    pooh.kekenyangan = 50
    
    # makan
    oyen.makan(ikan)
    oggy.makan(daging)
    pooh.makan(bamboo)
    
    # Asosiasi: beli item dari shop, menggunakan objek player dan itemsebagai parameter
    # Komposisi: setelah beli item, akan mendapatkan detail tranksaksi yang merupakan objek dari class Transaksi, namun objeknya dibuat hanya ketika beli item, dan akan hilang ketika objek shop dihapus
    shop.beli_item(player, air, 2)
    shop.beli_item(player, susu, 1)
    shop.beli_item(player, jus, 1)
    
    # atur haus pet ke 50 biar bisa minum
    oyen.haus = 50
    oggy.haus = 50
    pooh.haus = 50
    
    # minum
    oyen.minum(air)
    oggy.minum(susu)
    pooh.minum(jus)
    
    # tampilkan info item (overriding method)
    ikan.tampilkan_info_item()
    ayam.tampilkan_info_item()
    daging.tampilkan_info_item()
    bamboo.tampilkan_info_item()
    air.tampilkan_info_item()
    susu.tampilkan_info_item()
    jus.tampilkan_info_item()
    
    # bikin objek penyakit (untuk sekarang objek ini belum kepake buat apa apa)
    penyakit1 = Disease("P001", "Flu", "Penyakit yang menyebabkan demam dan batuk")
    penyakit2 = Disease("P002", "Diare", "Penyakit yang menyebabkan BAB cair")
    
    penyakit1.tampilkan_info_penyakit()
    penyakit2.tampilkan_info_penyakit()
    