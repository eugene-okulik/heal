from pages.base_page import BasePage


class ProductPage(BasePage):
    URL = 'http://testshop.qa-practice.com/shop/customizable-desk-9#attr=1,3'

    def click_add_to_cart(self):
        # self.find('#add_to_cart').click()
        self.find('#cart_add', description="Add to cart button").click()
