import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/"

data = []

url = base_url

ratings = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

while url:

    print("Scraping :", url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text.strip()
        price = price.replace("£", "").replace("Â", "").strip()
        price = float(price)

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        rating_text = book.p["class"][1]
        rating = ratings[rating_text]

        data.append({
            "Titre": title,
            "Prix_GBP": price,
            "Disponibilite": availability,
            "Note": rating
        })

    next_button = soup.find("li", class_="next")

    if next_button:
        next_page = next_button.a["href"]

        if url == base_url:
            url = base_url + next_page
        else:
            current_page = url.rsplit("/", 1)[0] + "/"
            url = current_page + next_page
    else:
        url = None


df = pd.DataFrame(data)

df.to_csv(
    "dataset.csv",
    index=False,
    encoding="utf-8-sig"
)

print("--------------------------------")
print("SCRAPING TERMINÉ !")
print("Nombre total de livres :", len(df))
print("Dataset enregistré dans dataset.csv")
print("--------------------------------")