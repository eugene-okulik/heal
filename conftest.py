import logging
import pytest

from pages.product_page import ProductPage

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")


@pytest.fixture
def product_page(page):
    return ProductPage(page)
