from bs4 import BeautifulSoup
import requests, openpyxl
import csv

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Scraped Data"
sheet.append(['Name', 'Price', 'Rating'])


try:
    source = requests.get("https://webscraper.io/test-sites/e-commerce/static")
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')
    print(soup)

    product_elements = soup.find_all(class_="product")
    product_data = []
    for product in product_elements:
        print(product)
        name = product.find(class_="product-name").text.strip()
        print(name)
        price = float(product.find(class_="product-price").text.strip().replace("$", ""))
        print(price)
        rating = float(product.find(class_="product-rating").text.strip())
        print(rating)

        product_data.append([name, price, rating])

        with open("products.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name",   "Price",   "Rating"])
            writer.writerows(product_data)
            break

except Exception as e:
    print(e)

excel.save("products.csv")


