from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-info div strong")