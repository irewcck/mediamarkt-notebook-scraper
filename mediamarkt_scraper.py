from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Tarayıcıyı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# MediaMarkt ana sayfasına git
driver.get("https://www.mediamarkt.com.tr/")
wait = WebDriverWait(driver, 20)

# Arama kutusunun yüklenmesini bekle
search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]')))
actions = ActionChains(driver)
actions.move_to_element(search_box).click().send_keys("notebook").send_keys(Keys.ENTER).perform()

# Ürünlerin yüklenmesini bekle
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article[data-test="mms-product-card"]')))
time.sleep(2)

# Sayfayı kaydırarak ürünleri tamamen yükle
SCROLL_PAUSE_TIME = 1.5
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Ürünleri bul
products = driver.find_elements(By.CSS_SELECTOR, 'article[data-test="mms-product-card"]')

urunler = []

for product in products[:10]:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'p[data-test="product-title"]').text.strip()
        try:
            price = product.find_element(By.CSS_SELECTOR, 'sc-b350c14-0 hPzUpv notranslate').text.strip()
        except:
            price = "Fiyat Bulunamadı"
        urunler.append((name, price))
    except Exception as e:
        print(f"Ürün atlandı: {e}")
        continue


#------------------------------------------



# Sayfa tamamen yüklendikten sonra yıldız filtresine ulaşmak için biraz bekleyelim
time.sleep(2)

# 4 yıldız filtresini aç (Details etiketini tıklatmak gerekebilir)
try:
    # Filtre bölümünü aç (Details)
    star_filter = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#filter > div > details:nth-child(21)')))
    driver.execute_script("arguments[0].scrollIntoView();", star_filter)
    time.sleep(1)
    star_filter.click()
    time.sleep(1)

    # 4 yıldız kutucuğunu bul ve tıkla (label for="4")
    star_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="4"]')))
    driver.execute_script("arguments[0].click();", star_checkbox)
    time.sleep(3)

except Exception as e:
    print(f"Yıldız filtresi uygulanamadı: {e}")




# Ürünlerin tekrar yüklenmesini bekle
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article[data-test="mms-product-card"]')))
time.sleep(2)

# Sayfayı kaydırarak ürünleri tamamen yükle
SCROLL_PAUSE_TIME = 1.5
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Ürünleri bul ve yazdır
# Ürünleri bul ve yazdır
products = driver.find_elements(By.CSS_SELECTOR, 'article[data-test="mms-product-card"]')
urunler = []

for product in products[:10]:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'p[data-test="product-title"]').text.strip()
        try:
            # Class'lar arası boşluk olduğu için CSS selector olarak nokta (.) ile bağlayarak yazıyoruz
            price = product.find_element(By.CSS_SELECTOR, '.sc-b350c14-0.hPzUpv.notranslate').text.strip()
        except:
            price = "Fiyat Bulunamadı"
        urunler.append((name, price))
    except Exception as e:
        print(f"Ürün atlandı: {e}")
        continue

# Sonuçları yazdır
for i, (isim, fiyat) in enumerate(urunler, 1):
    print(f"{i}. Ürün: {isim} - {fiyat}")

# Dosyaya yaz
with open("urunler.txt", "w", encoding="utf-8") as f:
    for name, price in urunler:
        f.write(f"{name} - {price}\n")

print(f"{len(urunler)} ürün başarıyla 'urunler.txt' dosyasına yazıldı.")
input("Programı kapatmak için Enter'a bas...")
driver.quit()
