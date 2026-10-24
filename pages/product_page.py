import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class ProductPage(BasePage):
    URL = 'http://testshop.qa-practice.com/shop/customizable-desk-9#attr=1,3'
    SHOP_URL = 'http://testshop.qa-practice.com/'

    def open_shop(self):
        self.page.goto(self.SHOP_URL)

    def open_first_product(self):
        first_product = self.find("form.oe_product_cart", description="First product card")
        name = first_product.locator('a[itemprop="name"]').inner_text().strip()
        first_product.locator("a.oe_product_image_link").click()
        expect(self.page.locator("h1")).to_have_text(name)
        return name

    def click_add_to_cart(self):
        self.find_by_role("button", "Add to cart", description="Add to cart button").click()

    def confirm_add_to_cart(self, product_name):
        dialog = self.find_by_role("dialog", "", description="Add to cart dialog")
        expect(dialog).to_be_visible()
        expect(dialog.locator("table")).to_contain_text(product_name)
        self.find_child_by_role(dialog, "button", "Continue Shopping", description="Continue Shopping button").click()
        expect(dialog).to_be_hidden()
        self.page.wait_for_load_state("networkidle")

    def open_cart(self):
        self.find('a[href="/shop/cart"]', description="Cart link").click()
        expect(self.page).to_have_url(re.compile(r"/shop/cart"))
