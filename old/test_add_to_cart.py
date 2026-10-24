import re

from playwright.sync_api import Page, expect


def test_add_first_product_to_cart(page: Page):
    # 1. Зайти на сайт
    page.goto("http://testshop.qa-practice.com/")

    # 2. Нажать на первый товар на странице
    first_product = page.locator("form.oe_product_cart").first
    name = first_product.locator('a[itemprop="name"]').inner_text().strip()
    first_product.locator("a.oe_product_image_link").click()
    expect(page.locator("h1")).to_have_text(name)

    # 3. Добавить товар в корзину
    page.get_by_role("button", name="Add to cart").click()
    dialog = page.get_by_role("dialog")
    expect(dialog).to_be_visible()
    expect(dialog.locator("table")).to_contain_text(name)
    dialog.get_by_role("button", name="Continue Shopping").click()
    expect(dialog).to_be_hidden()
    # дождаться завершения POST /shop/cart/update_option
    page.wait_for_load_state("networkidle")

    # 4. Открыть корзину и проверить, что товар в ней
    page.locator('a[href="/shop/cart"]').first.click()
    expect(page).to_have_url(re.compile(r"/shop/cart"))
    line = page.locator(".o_cart_product").first
    expect(line).to_contain_text(name)
