import requests


def parse_wb(query):
    url = f" https://search.wb.ru/exactmatch/ru/common/v4/search?query={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0 "
                      "Safari/537.36",
        "Accept": "*/*"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        products = []
        for item in data.get("data", {}).get("products", []):
            name = item.get("name")
            price_u = item.get("priceU")
            sale_price_u = item.get("salePriceU")
            rating = item.get("rating", 0)
            review_count = item.get("reviewCount", 0)

            products.append({
                "name": name,
                "price": price_u // 100 if price_u else 0,
                "sale_price": sale_price_u // 100 if sale_price_u else 0,
                "rating": float(rating),
                "reviews": int(review_count)
            })

        return products

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print("Response status code:", response.status_code)
        print("Response text:", response.text)
        return []
    except Exception as e:
        print(f"Other error: {e}")
        return []
