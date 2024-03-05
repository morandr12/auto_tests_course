"""Модуль содержит линки на страницы"""

MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"
LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"

PRODUCTS_PAGE_LINKS_LIST = [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/",
] + [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(i)
    for i in range(10)
]
