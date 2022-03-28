from random import randint
from selenium.webdriver.common.keys import Keys
import time
from page_kapcsolat import ContactForm


# test data
random_email = randint(1, 100)
user_data = ["Teszt", "Elek", f'belaatester+user{random_email}@gmail.com', "Ajánlatkérés", "Teszt homepage Chrome"]
expected_msg = 'Thank you for your message. We will get in touch with you shortly'


# tc01-fill form
def test_tc01_fill_form():
    form = ContactForm()
    form.fill_input_fields(user_data, form.field_id, form.submit_xp)
    time.sleep(2)
    assert form.locator_by_id(form.field_id[5]).text == form.expected_msg
