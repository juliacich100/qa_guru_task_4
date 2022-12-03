def make_more_readable(some_function, *args):
    nice_name = some_function.__name__.replace('_', ' ').capitalize()
    print(nice_name, *args)


def open_browser(browser_name='Chrome'):
    make_more_readable(open_browser, browser_name)


def go_to_companyname_homepage(page_url="mail.ru"):
    make_more_readable(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url='mail.ru', button_text='Регистрация'):
    make_more_readable(find_registration_button_on_login_page, page_url, button_text)


open_browser()
go_to_companyname_homepage()
find_registration_button_on_login_page()