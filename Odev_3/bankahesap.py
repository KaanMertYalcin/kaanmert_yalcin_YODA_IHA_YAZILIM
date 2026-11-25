class Hesap:
    def __init__(self, hesap_sahibi, hesap_no, bakiye=0.0):
        self.hesap_sahibi = hesap_sahibi
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz tutar girdiniz.")

    def para_cek(self, miktar):
        if miktar <= 0:
            print("Geçersiz tutar girdiniz.")
        elif miktar > self.bakiye:
            print("Yetersiz bakiye.")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")

    def bakiye_goruntule(self):
        print(f"Hesap Sahibi: {self.hesap_sahibi} | Hesap No: {self.hesap_no} | Güncel Bakiye: {self.bakiye} TL")


ad_soyad = input("Hesap sahibinin adı ve soyadı: ")
hesap_numarasi = input("Hesap numarası: ")
baslangic_bakiye = float(input("Başlangıç bakiyesi (TL): "))

hesap = Hesap(ad_soyad, hesap_numarasi, baslangic_bakiye)

while True:
    print("\n1 - Para Yatır")
    print("2 - Para Çek")
    print("3 - Bakiye Görüntüle")
    print("4 - Çıkış")

    secim = input("İşlem seçiniz (1-4): ")

    if secim == "1":
        tutar = float(input("Yatırılacak tutar: "))
        hesap.para_yatir(tutar)
    elif secim == "2":
        tutar = float(input("Çekilecek tutar: "))
        hesap.para_cek(tutar)
    elif secim == "3":
        hesap.bakiye_goruntule()
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")