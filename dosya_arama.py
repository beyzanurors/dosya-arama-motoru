import os

ana_klasor = "C:/Users/meryemce/OneDrive/Desktop/Ayıklanacak"

aranan_dosya = input("Aratmak istediğin dosyanın adını yaz (örn: rapor.pdf): ")

bulundu_mu = False

for kok, klasorler, dosyalar in os.walk(ana_klasor):
  if aranan_dosya in dosyalar:
    bulundu_mu = True
    tam_konum = os.path.join(kok, aranan_dosya)

    print("\n Harika, dosya bulundu!")
    print(f" Dosyanın Tam Yolu: {tam_konum}")
    break  

if not bulundu_mu:
  print(f"\n Maalesef '{aranan_dosya}' adında bir dosya bulunamadı.")