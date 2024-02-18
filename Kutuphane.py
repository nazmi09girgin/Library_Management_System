class Kutuphane:
    def __init__(self, dosya_adi="books.txt"):
        self.dosya_adi = dosya_adi
        self.file = open(self.dosya_adi, "a+")
    
    def __del__(self):
        self.file.close()

    def kitap_listele(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        if not lines:
            print("Kitap bulunmamaktadır.")
        else:
            for line in lines:
                kitap_bilgisi = line.split(",")
                print("Kitap Adı: {} - Yazar: {}".format(kitap_bilgisi[0], kitap_bilgisi[1]))


    def kitap_ekle(self):
        kitap_adi = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        yayin_tarihi = input("Yayın Tarihi:")
        sayfa_sayisi = input("Sayfa Sayısı:")
        kitap_bilgisi = "{},{},{},{}".format(kitap_adi, yazar, yayin_tarihi, sayfa_sayisi)

        self.file.seek(0)
        lines = self.file.readlines()

        for line in lines:
            if kitap_adi in line and yazar in line:
                print("Bu kitap zaten mevcut. Eklenemedi.")
                return
            
        self.file.write(kitap_bilgisi + "\n")
        print("Kitap başarıyla eklendi")

    def kitap_sil(self):
        silinecek_kitap = input("Silmek istediğiniz1 kitap adı: ")
        self.file.seek(0)
        lines = self.file.readlines()

        self.file.seek(0)
        self.file.truncate()

        kitap_var_mi = False  
        for line in lines:
            if silinecek_kitap not in line:
                self.file.write(line)
            else:
                kitap_var_mi = True  

        if kitap_var_mi:
            print("Kitap silindi")
        else:
            print("Kitap bulunamadı. Silme işlemi başarısız.")


lib = Kutuphane()
while True:
    print("""
*** MENÜ ***
1) Kitapları Listele
2) Kitap Ekle
3) Kitap Sil
4) Çıkış
""")

    islem = input("Yapmak istediğiniz işlemi seçiniz: ")
    if islem == "1":
        lib.kitap_listele()
    elif islem == "2":
        lib.kitap_ekle()
    elif islem == "3":
        lib.kitap_sil()
    elif islem == "4":
        print("Çıkış yapılıyor")
        break
    else:
        print("Geçersiz işlem")
      