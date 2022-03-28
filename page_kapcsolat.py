from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


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
        self.field_id = ['ff_1_names_first_name_', 'ff_1_names_last_name_', 'ff_1_email', 'ff_1_subject',
                         'ff_1_message', 'fluentform_1_success']
        self.submit_xp = '//button[@type="submit"]'

    def locator_by_id(self, id_name):
        element = self.driver.find_element(By.ID, id_name)
        return element

    def locator_by_xp(self, xp):
        element = self.driver.find_element(By.XPATH, xp)
        return element

    def fill_input_fields(self, my_list, field_list, btn):  # fill in form input fields
        for _ in range(len(my_list)):
            self.locator_by_id(field_list[_]).send_keys(my_list[_])
        time.sleep(2)
        self.locator_by_xp(btn).click()

    def teardown(self):
        self.driver.close()
