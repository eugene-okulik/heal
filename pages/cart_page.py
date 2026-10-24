from pages.base_page import BasePage


class CartPage(BasePage):
    URL = 'http://testshop.qa-practice.com/shop/cart'

    def open_cart(self):
        self.open()

    def get_first_line(self):
        return self.find(".o_cart_product", description="Cart product line")
