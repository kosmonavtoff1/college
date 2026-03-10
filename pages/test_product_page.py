from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    # Новая ссылка на другой товар
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    # 1. Запоминаем название и цену ДО добавления
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # 2. Выполняем действие
    page.add_to_basket()
    page.solve_quiz_and_get_code() # Решаем математическую загадку

    # 3. Проверяем результат, используя сохраненные данные
    page.should_be_success_message(product_name)
    page.should_be_basket_total(product_price)