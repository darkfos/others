import pandas as pd
import time
import re

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

class ParseOzon:

    def __init__(self, item: str, number_page: int = 5):
        """
        Инициализация данных
        """

        self.item = item
        self.number_page = number_page
        self.data_tovars: dict = dict()
    
    def get_all_products(self) -> dict:
        """
        Получаем список всех книг.
        """
        
        with sync_playwright() as prs:
            #Создаем браузер
            self.browser = prs.firefox.launch(headless=False)
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
            self.page.goto("https://www.ozon.ru/")
            time.sleep(1.5)

            #Поиск по placeholder
            self.page.get_by_placeholder(text="Искать на Ozon").type(text=self.item, delay=0.4)

            #Нажатие кнопки - отправка submit
            self.page.query_selector("button[type='submit']").click()
            
            #Собираем ссылки на все товары
            self.get_links_books()

    def get_links_books(self):
        self.page.wait_for_selector("#paginatorContent")
        self.page_down(page_to_down=self.page)
        self.page.wait_for_selector(f":text('Дальше')")

        result_find = self.page.query_selector("#paginatorContent")
        links = result_find.query_selector_all(".tile-hover-target")
        
        list_link = list()
        id_c = 0

        #Проходимся по каждой ссылке
        for link in links:

            if id_c >= self.number_page:
                break
            if link.get_attribute("href") not in list_link:
                url = "https://www.ozon.ru" + link.get_attribute("href")
                self.get_info_book(url=url)

                list_link.append(link.get_attribute("href"))
                id_c += 1

            else:
                continue

        #Закрываем браузер после окончания работы
        self.browser.close()

        #Вызываем метод для записи данных в Excel
        self.save_to_xsls()

    def page_down(self, page_to_down):
        """
        Спускаемся в дно страницы
        """
    
        page_to_down.evaluate("""
                                const scrollStep = 200;
                                const scrollInterval = 100;
                            
                                const scrollHeight = document.documentElement.scrollHeight;
                                let currentPosition = 0;
                                const interval = setInterval(() => {
                                    window.scrollBy(0, scrollStep);
                                    currentPosition += scrollStep;

                                    if (currentPosition >= scrollHeight) {
                                        clearInterval(interval);
                                    }
                                }, scrollInterval);
                           """)

    def get_info_book(self, url: str):
        """
        Получаем информацию о товаре
        """
        
        #Открываем страницу по ссылке.
        self.new_page = self.context.new_page()
        self.new_page.goto(url=url)

        self.data_tovar: dict = dict()

        #Получаем нужные данные о товаре
        text: str = self.new_page.wait_for_selector("div[data-widget='webProductHeading']").inner_text()
        all_price_text = self.new_page.wait_for_selector("div[data-widget='webPrice']").inner_text().split("\n")
        character_book = self.new_page.wait_for_selector("div[data-widget='webCharacteristics']").inner_text().split("\n")
        price: str = "".join(re.findall(r"\d+", all_price_text[0]))

        characteristics_book: dict = dict()

        #Получаем описание книги
        count_id = 1
        for i in character_book:
            if i.lower() == "перейти к описанию":
                break
            if count_id % 2 != 0:
                characteristics_book[i] = ""
            else:
                characteristics_book[list(characteristics_book.keys())[-1]] = i
            count_id += 1
        
        self.new_page.close()

        self.data_tovars[text] = {
            "Название товара": text,
            "Цена": price,
            "Характеристика": characteristics_book,
            "Ссылка": url
        }


        
    def save_to_xsls(self):
        """
        Сохраняем данные в csv файл
        """

        all_columns = ["Название товара", "Цена", "ISBN", "Год выпуска", "Издательство", "Язык издания", "Возрастные ограничения", "Ссылка"]

        #Создаем DataFrame
        df_tovars = pd.DataFrame(columns=all_columns)

        #Заполняем DataFrame
        for indx in range(len(self.data_tovars)):
            for tovar in list(self.data_tovars.keys()):
                for data_tovar in list(self.data_tovars.get(tovar).keys()):
                    if data_tovar == "Характеристика":
                        for chr_t in list(self.data_tovars.get(tovar).get(data_tovar).keys()):
                            df_tovars.loc[indx, chr_t] = self.data_tovars.get(tovar).get(data_tovar).get(chr_t)
                    else:
                        df_tovars.loc[indx, data_tovar] = self.data_tovars.get(tovar).get(data_tovar)
        
        #Сохраняем DataFrame
        df_tovars.to_csv(f"parse_ozon/all_books.csv")


ozon_parser: ParseOzon = ParseOzon("Python")
ozon_parser.get_all_products()
