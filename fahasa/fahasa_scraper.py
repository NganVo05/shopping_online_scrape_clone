from bs4 import BeautifulSoup
from bs4.element import ResultSet
from driver.driver import create_web_driver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_product_names(soup: BeautifulSoup) -> ResultSet:
    selector = '#products_grid .product-name-no-ellipsis a'
    name_items = soup.select(selector=selector)
    return name_items


def get_product_info(soup: BeautifulSoup) -> str:
    name_items = get_product_names(soup=soup)

    for index in range(len(name_items)):
        # index = index + 31
        # if(index > 31): return
        try:
            unknow_url = "https://cdn0.fahasa.com/skin/frontend/ma_vanese/fahasa/images/ring_loader.gif"
            product_url = name_items[index].get('href')

            print("\n\n  product_url:::::::" + product_url + "\n\n")    

            if unknow_url in product_url:
                # Xoá chuỗi "https://cdn0.fahasa.com/skin/frontend/ma_vanese/fahasa/images/ring_loader.gif" và dấu khoảng trắng sau đó
                product_url = product_url.replace(unknow_url, "").strip()

            browser = create_web_driver(product_url, "fahasa")
            # Đợi 1 giây
            html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            soup1 = BeautifulSoup(html, "html.parser")

            try:
                # 2 Image
                imageUrl = "null"
                image = soup1.select(selector="#image")
                if len(image) > 0:
                    imageUrl = image[0].get("data-src")
                    if unknow_url in imageUrl:
                        imageUrl = imageUrl.replace(unknow_url, "").strip()
                        if(len(imageUrl) == 0): imageUrl = "null"
                else: continue

                #3 Title
                title = "null"
                title = soup1.select(selector=".product-essential-detail h1")
                if len(title) == 0:
                    title = f'"null"'
                else:
                    title = f'"{title[0].text}"'

                # 4 rating
                rating = "null"
                rating_element = soup1.select(selector=".ratings-mobile .icon-star-text")
                if len(rating_element) > 0:
                    rating = f'"{rating_element[0].text}"'
                

                # 5 numratings
                numratings = "null"
                numratings = soup1.select(selector=".ratings-desktop .rating-links a")
                if len(numratings) == 0:
                    numratings = f'"null"'
                else:
                    numratings = f'"{numratings[0].text}"'

                # 6 des
                des = "null"
                des = soup1.select(selector="#desc_content")
                if len(des) == 0:
                    des = f'"null"'
                else:
                    des = des[0].text.replace('"', '')
                    des = f'"{des}"'


                # 7 data_supplier
                data_supplier = "null"
                data_supplier = soup1.select(selector=".data_supplier")
                if len(data_supplier) == 0:
                    data_supplier = f'"null"'
                else:
                    data_supplier = f'"{data_supplier[0].text}"'

                # 8 data_author
                data_author = "null"
                data_author = soup1.select(selector=".data_author")
                if len(data_author) == 0:
                    data_author = f'"null"'
                else:
                    data_author = f'"{data_author[0].text}"'

                # 9 data_publisher
                data_publisher = "null"
                data_publisher = soup1.select(selector=".data_publisher")
                if len(data_publisher) == 0:
                    data_publisher = f'"null"'
                else:
                    data_publisher = f'"{data_publisher[0].text}"'


                # 10 data_publish_year
                data_publish_year = "null"
                data_publish_year = soup1.select(selector=".data_publish_year")
                if len(data_publish_year) == 0:
                    data_publish_year = f'"null"'
                else:
                    data_publish_year = f'"{data_publish_year[0].text}"'

                # 11 data_size
                data_size = "null"
                data_size = soup1.select(selector=".data_size")
                if len(data_size) == 0:
                    data_size = f'"null"'
                else:
                    data_size = f'"{data_size[0].text}"'

                # 12 data_book_layout
                data_book_layout = "null"
                data_book_layout = soup1.select(selector=".data_book_layout")
                if len(data_book_layout) == 0:
                    data_book_layout = f'"null"'
                else:
                    data_book_layout = f'"{data_book_layout[0].text}"'

                # 13 data_qty_of_page
                data_qty_of_page = "null"
                data_qty_of_page = soup1.select(selector=".data_qty_of_page")
                if len(data_qty_of_page) == 0:
                    data_qty_of_page = f'"null"'
                else:
                    data_qty_of_page = f'"{data_qty_of_page[0].text}"'

                # 14 cate0
                cate0 = "null"
                cate0 = soup1.select(".breadcrumb li:nth-child(1) a")
                if len(cate0) == 0:
                    cate0 = f'"null"'
                else:
                    cate0 = f'"{cate0[0].text}"'

                # 15 cate1
                cate1 = "null"
                cate1 = soup1.select(".breadcrumb li:nth-child(2) a")
                if len(cate1) == 0:
                    cate1 = f'"null"'
                else:
                    cate1 = f'"{cate1[0].text}"'

                # 16 cate2
                cate2 = "null"
                cate2 = soup1.select(".breadcrumb li:nth-child(3) a")
                if len(cate2) == 0:
                    cate2 = f'"null"'
                else:
                    cate2 = f'"{cate2[0].text}"'

                # 17 cate3
                cate3 = "null"
                cate3 = soup1.select(".breadcrumb li:nth-child(4) a")
                if len(cate3) == 0:
                    cate3 = f'"null"'
                else:
                    cate3 = f'"{cate3[0].text}"'

                # 18 special-price
                price_s = "null"
                price_s = soup1.select(selector=".special-price .price")
                if len(price_s) == 0:
                    price_s = f'"0"'
                else:
                    price_s = f'"{price_s[0].text}"'

                # 19 old-price
                price_o = ""
                price_o = soup1.select(selector=".old-price .price")
                if len(price_o) == 0:
                    price_o = f'"0"'
                else:
                    price_o = f'"{price_o[0].text}"'

                product_info = "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18}\n".format(product_url, imageUrl, title, rating, numratings, data_supplier, data_author, data_publisher, data_publish_year, data_size, data_book_layout, des, data_qty_of_page, cate0, cate1, cate2, cate3, price_s, price_o)
                
                # print(product_url, "\n", imageUrl, "\n", title, "\n", rating, "\n", numratings, "\n", data_supplier, "\n", data_author, "\n", data_publisher, "\n", data_publish_year, "\n", data_size, "\n", data_book_layout, "\n", des, "\n", data_qty_of_page, "\n", cate0, "\n", cate1, "\n", cate2, "\n", cate3, "\n", price_s, "\n", price_o)

                yield product_info

                print("Product:::NUM::: ", index, ":::========================================================================")


            except Exception as e:
                print(f"Error processing product information: {e}")
                continue  # Tiếp tục vòng lặp nếu gặp lỗi

        except Exception as e:
            print(f"Error processing product: {e}")
            continue  # Tiếp tục vòng lặp nếu gặp lỗi










# def get_product_info(soup: BeautifulSoup) -> str:
#     name_items = get_product_names(soup=soup)

#     for index in range(len(name_items)):
#         browser = create_web_driver(name_items[index].get('href'), "fahasa")
#         html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
#         soup1 = BeautifulSoup(html, "html.parser")

#         # 2 Image
#         imageUrl=""
#         image = soup1.select(selector="#image")
#         if len(image) > 0:
#             imageUrl = image[0].get("src")

#         #3 Title
#         title = soup1.select(selector=".product-essential-detail h1")
#         if len(title) == 0:
#             title = f'" "'
#         else:
#             title = f'"{title[0].text}"'

#         # 4 rating
#         rating = "0"
#         rating_element = soup1.select(selector=".ratings-mobile .icon-star-text")
#         if len(rating_element) > 0:
#             rating = f'"{rating_element[0].text}"'
        

#         # 5 numratings
#         numratings = soup1.select(selector=".ratings-desktop .rating-links a")
#         if len(numratings) == 0:
#             numratings = f'" "'
#         else:
#             numratings = f'"{numratings[0].text}"'

#         # 6 des
#         des = soup1.select(selector="#desc_content")
#         if len(des) == 0:
#             des = f'" "'
#         else:
#             des = f'"{des[0].text}"'

#         # 7 data_supplier
#         data_supplier = soup1.select(selector=".data_supplier")
#         if len(data_supplier) == 0:
#             data_supplier = f'" "'
#         else:
#             data_supplier = f'"{data_supplier[0].text}"'

#         # 8 data_author
#         data_author = soup1.select(selector=".data_author")
#         if len(data_author) == 0:
#             data_author = f'" "'
#         else:
#             data_author = f'"{data_author[0].text}"'

#         # 9 data_publisher
#         data_publisher = soup1.select(selector=".data_publisher")
#         if len(data_publisher) == 0:
#             data_publisher = f'" "'
#         else:
#             data_publisher = f'"{data_publisher[0].text}"'


#         # 10 data_publish_year
#         data_publish_year = soup1.select(selector=".data_publish_year")
#         if len(data_publish_year) == 0:
#             data_publish_year = f'" "'
#         else:
#             data_publish_year = f'"{data_publish_year[0].text}"'

#         # 11 data_size
#         data_size = soup1.select(selector=".data_size")
#         if len(data_size) == 0:
#             data_size = f'" "'
#         else:
#             data_size = f'"{data_size[0].text}"'

#         # 12 data_book_layout
#         data_book_layout = soup1.select(selector=".data_book_layout")
#         if len(data_book_layout) == 0:
#             data_book_layout = f'" "'
#         else:
#             data_book_layout = f'"{data_book_layout[0].text}"'

#         # 13 data_qty_of_page
#         data_qty_of_page = soup1.select(selector=".data_qty_of_page")
#         if len(data_qty_of_page) == 0:
#             data_qty_of_page = f'" "'
#         else:
#             data_qty_of_page = f'"{data_qty_of_page[0].text}"'

#         # 14 cate0
#         cate0 = soup1.select(".breadcrumb li:nth-child(1) a")
#         if len(cate0) == 0:
#             cate0 = f'" "'
#         else:
#             cate0 = f'"{cate0[0].text}"'

#         # 15 cate1
#         cate1 = soup1.select(".breadcrumb li:nth-child(2) a")
#         if len(cate1) == 0:
#             cate1 = f'" "'
#         else:
#             cate1 = f'"{cate1[0].text}"'

#         # 16 cate2
#         cate2 = soup1.select(".breadcrumb li:nth-child(3) a")
#         if len(cate2) == 0:
#             cate2 = f'" "'
#         else:
#             cate2 = f'"{cate2[0].text}"'

#         # 17 cate3
#         cate3 = soup1.select(".breadcrumb li:nth-child(4) a")
#         if len(cate3) == 0:
#             cate3 = f'" "'
#         else:
#             cate3 = f'"{cate3[0].text}"'

#         # 18 special-price
#         price_s = soup1.select(selector=".special-price .price")
#         if len(price_s) == 0:
#             price_s = f'"0"'
#         else:
#             price_s = f'"{price_s[0].text}"'

#         # 19 old-price
#         price_o = soup1.select(selector=".old-price .price")
#         if len(price_o) == 0:
#             price_o = f'"0"'
#         else:
#             price_o = f'"{price_o[0].text}"'

#         print("========================================================================")

#         product_info = "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18}\n".format(name_items[index].get('href'), imageUrl, title, rating, numratings, data_supplier, data_author, data_publisher, data_publish_year, data_size, data_book_layout, des, data_qty_of_page, cate0, cate1, cate2, cate3, price_s, price_o)
#         yield product_info