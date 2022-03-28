from random import randint
from page_kapcsolat import ContactForm

# test data
random_email = randint(1, 100)
user_data = ["Teszt", "Elek", f'belaatester+user{random_email}@gmail.com', "Ajánlatkérés", "Teszt homepage Chrome"]


# tc01-fill form
def test_tc01_fill_form():
    form = ContactForm()
    field_list = form.locators_tag_name(form.input_fields_tag_name)
    # make a full list, with textarea
    field_list.insert(4, form.locator_by_name(form.text_area_tag_name))

    form.fill_input_fields(user_data, field_list, form.submit_tag_name)
