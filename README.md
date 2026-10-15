
#  Python File Search Engine (Dosya Arama Motoru)

Bu proje, bilgisayarınızda belirlediğiniz bir ana klasör ve alt klasörleri içerisinde hızlıca arama yaparak aradığınız dosyanın var olup olmadığını kontrol eden ve varsa tam konumunu (yolunu) ekrana yazdıran pratik bir Python otomasyon betiğidir.

##  Özellikler
- Belirtilen dizindeki tüm alt klasörleri (`os.walk` ile) köşe bucak tarar.
- Kullanıcıdan dinamik olarak aratmak istediği dosya adını alır (`input`).
- Dosya bulunduğunda tam dosya yolunu ekrana yazdırır ve aramayı sonlandırır.

## Kullanılan Teknolojiler
- **Python** (Temel döngüler ve koşullar)
- **OS Modülü** (İşletim sistemi ve dosya yolu yönetimi için)

##  Nasıl Çalıştırılır?
1. Bilgisayarınızda Python yüklü olduğundan emin olun.
2. Kod içerisindeki `ana_klasor` değişkenini kendi bilgisayarınızdaki bir klasör yoluyla güncelleyin.
3. Terminalde kodu çalıştırın:
   ```bash
   python file_searcher.py
