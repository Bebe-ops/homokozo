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
        self.locators = [{'first_name_id': 'ff_1_names_first_name_'}, {'last_name_id': 'ff_1_names_last_name_'},
                    {'email_id': 'ff_1_email'}, {'subject_id': 'ff_1_subject'}, {'message_id': 'ff_1_message'}]
        self.submit_xp = '//button[@type="submit"]'

    def locator_by_id(self, id_name):
        element = self.driver.find_element(By.ID, id_name)
        return element

    def locator_by_xp(self, xp):
        element = self.driver.find_element(By.XPATH, xp)
        return element

    def fill_input_field(self, my_id, test_data):
        self.locator_by_id(my_id).send_keys(test_data)

    def teardown(self):
        self.driver.close()
