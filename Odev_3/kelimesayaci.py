metin = input("Lütfen bir cümle veya paragraf girin: ")

toplam_karakter = len(metin)
kucuk_metin = metin.lower()

noktalama = ".,!?;:\"'()-[]"
temiz_metin = kucuk_metin
for isaret in noktalama:
    temiz_metin = temiz_metin.replace(isaret, "")

kelimeler = temiz_metin.split()
toplam_kelime = len(kelimeler)

if toplam_kelime == 0:
    print("Girdiğiniz metinde sayılacak bir kelime bulunamadı.")
else:
    en_uzun_uzunluk = 0
    kelime_tekrarlari = {}

    for kelime in kelimeler:
        if len(kelime) > en_uzun_uzunluk:
            en_uzun_uzunluk = len(kelime)

        if kelime in kelime_tekrarlari:
            kelime_tekrarlari[kelime] += 1
        else:
            kelime_tekrarlari[kelime] = 1

    print("\n--- Metin Analiz Sonuçları ---")
    print(f"Toplam kelime sayısı: {toplam_kelime}")
    print(f"Toplam karakter sayısı (boşluklar dahil): {toplam_karakter}")
    print(f"En uzun kelimenin uzunluğu: {en_uzun_uzunluk}")
    print("Kelime tekrar sayıları:")

    for kelime, adet in kelime_tekrarlari.items():
        print(f"  - {kelime}: {adet} kez")