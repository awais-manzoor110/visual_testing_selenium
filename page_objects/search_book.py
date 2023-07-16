from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    search_b = (By.ID, "searchBar")
    products = (By.CSS_SELECTOR, "#productList li a h2")

    def filter_books(self, search_text):
        element = self.driver.find_element(*SearchPage.search_b)
        return element.send_keys(search_text)

    def verify_visible_books_by_title(self, expected_title):
        elements = self.driver.find_elements(*SearchPage.products)
        for element in elements:
            if expected_title in element.text:
                return True

        return False
