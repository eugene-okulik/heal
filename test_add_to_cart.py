from playwright.sync_api import expect


def test_add_first_product_to_cart(product_page, cart_page):
    product_page.open_shop()
    name = product_page.open_first_product()

    product_page.click_add_to_cart()
    product_page.confirm_add_to_cart(name)

    product_page.open_cart()
    line = cart_page.get_first_line()
    expect(line).to_contain_text(name)
