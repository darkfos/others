import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.options import Options
import time
import csv


ALL_PRODUCTS: list[dict]= []


async def get_data_from_yandex(fx_driver: webdriver.Firefox):

    cnt: int = 0
    while cnt != 5:
        # Прокрутка вниз страницы
        fx_driver.execute_script(
          script="window.scrollBy(0, 2000);"
        )
        time.sleep(2.5)
        cnt += 1

    await product_partition(engine=fx_driver)


async def product_partition(engine: webdriver.Firefox):
    all_product_cards = engine.find_element(by=By.ID,
                                            value="/content/page/fancyPage/content/search/searchSerpStatic/content"
                                            )
    products = all_product_cards.find_elements(
        by=By.CSS_SELECTOR,
        value="[data-auto='searchOrganic']"
    )

    for product in products:
        # Переход на товар
        product_link = product.find_element(by=By.CSS_SELECTOR, value="[data-auto='snippet-link']")
        time.sleep(2)
        await product_data(url=product_link.get_attribute("href"))


async def product_data(url: str):
    engine = webdriver.Firefox()
    engine.get(url=url)

    title_product = engine.find_element(by=By.CSS_SELECTOR, value="[data-auto='productCardTitle']").text
    list_images_products = engine.find_elements(by=By.CSS_SELECTOR, value="[data-auto='media-viewer-thumbnails']")
    images: list[WebElement] = [
        image.find_elements(by=By.TAG_NAME, value="img")[0].get_attribute(name="src")
        for image in list_images_products
    ]
    description_product = engine.find_element(by=By.ID, value="product-description").text
    other_data = engine.find_element(by=By.CSS_SELECTOR, value="[data-apiary-widget-name='@card/SpecsListNewGrid']")

    old_data = ""
    attr_data = {}
    cnt: int = 0

    for data in other_data.find_elements(by=By.TAG_NAME, value="span"):
        if cnt % 2 == 0:
            attr_data[data.text] = ""
            old_data = data.text
        else:
            attr_data[old_data] = data.text
        cnt += 1

    print(attr_data)
    ALL_PRODUCTS.append(
        {
            "title_product": title_product,
            "description": description_product,
            "images": images,
            "other_data": attr_data
        }
    )

    engine.close()

async def load_data_to_csv() -> None:

    with (open("scooters24.csv", "w", newline="") as file):
        max_other_data_keys = max(ALL_PRODUCTS, key=lambda x: len(x["other_data"].keys()))
        keyses = {
            "title_product": "",
            "description": "",
            "images": []
        }

        keyses.update(max_other_data_keys.get("other_data"))

        csv_writer = csv.DictWriter(
            file,
            fieldnames=keyses.keys(),
            delimiter=','
        )

        # Сохранение результатов в csv файл
        csv_writer.writeheader()

        for product in ALL_PRODUCTS:
            new_product = {}
            # Установка данных
            for key in keyses.keys():
                if key in product.keys():
                    new_product[key] = product.get(key)
                elif key in product.get("other_data").keys():
                    new_product[key] = product.get("other_data").get(key)
                else:
                    new_product[key] = ""
            csv_writer.writerow(new_product)



async def main():
    try:
        firefox_driver_options: Options = Options()
        firefox_driver = webdriver.Firefox(
            options=firefox_driver_options
        )

        firefox_driver.get("https://market.yandex.ru/business--scooter-24/35256421?generalContext=t%3DshopInShop%3Bi%3D1%3Bbi%3D35256421%3B&rs=eJwzMv7EaMDBKLDwEKsEg8bWTac5NOZsBhKHZ09l1TgKYt0AiXWBWL9ArCtAlhOTAJsXh3lqioGxSaJJkJGhubGloYGZqYWRoYmZvrGRmbmRYZppYpqRabKJkXFqilGqQapJapKpUYqBmYGBvqG-IQDA4yWy&searchContext=sins_ctx")
        await get_data_from_yandex(firefox_driver)
        # Сохранение результатов в csv файл
        await load_data_to_csv()
        firefox_driver.close()
    except Exception as ex:
        await load_data_to_csv()
        print(ex)


if __name__ == "__main__":
    asyncio.run(main=main())
