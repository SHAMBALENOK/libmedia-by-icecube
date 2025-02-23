import requests
from bs4 import BeautifulSoup as BS

# url = 'https://www.kinopoisk.ru/film/535341/'
# class_ = 'styles_title__65Zwx styles_root__l9kHe styles_root__5sqsd styles_rootInDark__SZlor'
class_ = 'hero__primary-text'  # 'hero__primary-text'
url = 'https://www.imdb.com'

# url = 'https://yandex.ru/pogoda/kaliningrad'
# class_ = 'temp__value temp__value_with-unit'

while True:
    r = requests.get(url)

    html = BS(r.text, 'html.parser')
    # t = html.find('h1', class_)

    print(r)

    t = html.findAll('span')
    print(t)

    # if t is not None:
    #     break

print(t.text)
