# 🛒 MediaMarkt Notebook Scraper

Bu proje, MediaMarkt web sitesinden ⭐️ yıldız ve  müşteri yorumuna sahip **rastgele notebook ürünlerinin isimlerini ve fiyatlarını** çeken bir Python web scraping uygulamasıdır. Projede Selenium kütüphanesi kullanılarak sayfa üzerinde otomatik gezinme ve veri çekme işlemleri gerçekleştirilmiştir.

## 👩‍💻 Geliştirici
**İrem Çiçek**  

---

## 📌 Proje Adımları

1. MediaMarkt web sitesine otomatik olarak giriş yapılır.
2. Arama kısmına `notebook` yazılır.
3. Sayfa aşağıya kaydırılarak tüm ürünler yüklenir.
4. Sol menüden `4 yıldız ve üzeri` müşteri değerlendirmesi filtresi seçilir.
5. Sayfadaki ilk 10 ürünün:
   - Adı
   - Fiyatı  
   bilgileri çekilerek `urunler.txt` dosyasına yazılır.

---

## 💻 Kullanılan Teknolojiler

- **Python**
- **Selenium**
- **ChromeDriverManager**
- Web tarayıcısı otomasyonu
## 📷 Ekran Görselleri

Projenin ekran görüntüleri aşağıdaki PowerPoint dosyasındadır:

📎 [Görseller.pptx]


---

## 🚀 Kullanım

```bash
pip install selenium webdriver-manager
python mediamarkt_scraper.py
