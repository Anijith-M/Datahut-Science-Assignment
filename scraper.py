from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# 1. Setup browser
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# 2. Open website
url = "https://www.nike.com/in/w/womens-shoes-5e1x6zy7ok"
driver.get(url)
time.sleep(5)

# 3. Scroll to load products
for _ in range(8):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# 4. Find all product cards
products = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

data = []

for p in products:
    try:
        product_url = p.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        product_url = None

    try:
        name = p.find_element(By.CSS_SELECTOR, "div.product-card__title").text
    except:
        name = None

    try:
        price_text = p.find_element(By.CSS_SELECTOR, "div.product-price").text
        price_parts = price_text.replace("₹", "").replace(",", "").split("\n")
        if len(price_parts) == 2:
            sale_price, mrp = price_parts
        else:
            sale_price = price_parts[0]
            mrp = None
    except:
        sale_price = None
        mrp = None

    data.append({
        "url": product_url,
        "product_name": name,
        "brand": "Nike",
        "sale_price": sale_price,
        "mrp": mrp
    })

driver.quit()

df = pd.DataFrame(data)

# 1. Remove duplicate products
df.drop_duplicates(subset="url", inplace=True)

# 2. Remove rows with missing product_name or sale_price
df = df.dropna(subset=["product_name", "sale_price"])

# 3. Optional: clean price columns (remove ₹ and commas)
df["sale_price"] = df["sale_price"].str.replace("₹", "", regex=False).str.replace(",", "")
df["mrp"] = df["mrp"].str.replace("₹", "", regex=False).str.replace(",", "")

# 4. Save final CSV
df.to_csv("dataset.csv", index=False)

print("Saved", len(df), "products")


print("Saved", len(df), "products")
