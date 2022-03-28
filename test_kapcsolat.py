from random import randint
from selenium.webdriver.common.keys import Keys
import time
from page_kapcsolat import ContactForm


# test data
random_email = randint(1, 100)
user_data = ["Teszt", "Elek", f'belaatester+user{random_email}@gmail.com', "Ajánlatkérés", "Teszt homepage Chrome"]


# tc01-fill form
def test_tc01_fill_form():
    form = ContactForm()
    form.fill_input_field(form.locators[0]['first_name_id'], user_data[0])
    form.fill_input_field(form.locators[1]['last_name_id'], user_data[1])
    form.fill_input_field(form.locators[2]['email_id'], user_data[2])
    form.fill_input_field(form.locators[3]['subject_id'], user_data[3])
    form.fill_input_field(form.locators[4]['message_id'], user_data[4])
    time.sleep(2)
    form.locator_by_xp(form.submit_xp).send_keys(Keys.ENTER)
