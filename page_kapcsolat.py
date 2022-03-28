from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument('--headless')
# options.add_argument('--disable-gpu')


# Homepage-form
class ContactForm:
    def __init__(self):
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get('https://sandbox.develop.y-collective.hu/kapcsolat/')
        self.driver.maximize_window()
        self.input_fields_tag_name = 'input'
        self.text_area_tag_name = 'textarea'
        self.submit_tag_name = 'button'

    def locators_tag_name(self, tag):
        elements = self.driver.find_elements(By.TAG_NAME, tag)
        return elements

    def locator_by_name(self, tag):
        element = self.driver.find_element(By.TAG_NAME, tag)
        return element

    def fill_input_fields(self, my_list, field_list, btn):  # fill in form input fields
        for _ in range(len(my_list)):
            field_list[_].send_keys(my_list[_])
        self.locator_by_name(btn).click()
