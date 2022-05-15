import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://knijky.ru/seriya/garri-potter"




HEADESRS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Acent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'
}
@csrf_exempt
def get_html(url, params=''):
    reg = requests.get(url, headers=HEADESRS, params=params)
    return reg

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="views-row")
    book = []

    for item in items:
        book.append(
            {
                "title": item.find("div", class_="views-field views-field-title"),
                # "image": item.find('div', class_="img-product-block js__img-product-block").find('img').get('src')
                # "image": item.find('a').find('img').get('svg')
            }
        )
    return book


@csrf_exempt
def parser_func():
     html = get_html(HOST)
     if html.status_code == 200:
         book = []
         for page in range(2):
             html = get_html(HOST)
             book.extend(get_data(html.text))
         return book

#
# HOST2 = ""
#
#
# @csrf_exempt
# def get_html(url, params=''):
#     r = requests.get(url, headers=HEADESRS, params=params)
#     return r
#
# @csrf_exempt
# def get_data(html):
#     soup = BeautifulSoup(html, "html.parser")
#     items = soup.find_all("div", class_="views-row")
#     ranobe = []
#
#     for item in items:
#         ranobe.append(
#             {
#                 "title": item.find("a", class_="views-field views-field-title").get_text(),
#                 # "image": item.find('a', class_="ArticleItem--image").find('img').get('src')
#                 # "image": item.find('a').find('img').get('svg')
#             }
#         )
#     return ranobe
#
# @csrf_exempt
# def parser_func2():
#     html = get_html(HOST2)
#     if html.status_code == 200:
#          ranobe = []
#          for page in range(2, 3):
#              html = get_html(HOST2)
#              ranobe.extend(get_data(html.text))
#          return ranobe