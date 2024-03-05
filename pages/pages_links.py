"""Модуль содержит линки на страницы"""

MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"
LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"
PRODUCTS_PAGE_LINK_1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
PRODUCTS_PAGE_LINK_2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"
PRODUCTS_PAGE_PROMO_LINKS = [PRODUCTS_PAGE_LINK_1 + str(i) for i in range(10)]
PRODUCTS_PAGE_NEW_YEAR_PROMO_LINKS = [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
]
