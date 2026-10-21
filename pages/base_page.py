import logging

from playwright.sync_api import Page, Locator, TimeoutError as PlaywrightTimeoutError

from utils.healer import find_selector


class BasePage:
    URL = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.URL:
            self.page.goto(self.URL)
        else:
            raise NotImplementedError('This page doesn\'t have URL')

    def heal(func):

        def wrapper(self, *args, **kwargs):
            try:
                logging.info(f"Attempting to find element")
                return func(self, *args, **kwargs)
            except PlaywrightTimeoutError as e:
                element_description = kwargs.pop('description', None)
                params = (list(args))
                params.extend(kwargs.values())
                logging.info(f"Element was not found by {', '.join(params)}")
                if element_description:
                    dom = self.page.content()
                    selector = find_selector(params, description=element_description, dom=dom)
                    if selector:
                        return self.find(selector)
                    raise e
                else:
                    logging.error(
                        "Element healing impossible as element has no description or was not found after healing (see logs)")
                    raise e

        return wrapper

    @heal
    def find(self, selector, description=None) -> Locator:
        locator = self.page.locator(selector).first
        locator.wait_for(state="attached", timeout=3000)  # forces the lookup
        return locator

    @heal
    def find_by_role(self, role, title, description=None) -> Locator:
        locator =  self.page.get_by_role(role, name=title).first
        locator.wait_for(state="attached", timeout=3000)  # forces the lookup
        return locator
