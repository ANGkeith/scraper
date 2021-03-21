from time import sleep, time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from settings import env
from utils import retry_until_success, is_after_work, has_available_spot, send_message

send_message("Bot has started.")

while True:

    start = time()
    options = Options()
    options.add_argument("--headless")
    print("Opening browser")
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)

    driver.get(env("URL"))

    driver.find_element_by_css_selector(".one-fourth > a").click()

    driver.execute_script("""
        $('#welcome-window').modal('hide')
    """)

    retry_until_success(lambda : driver.find_elements_by_css_selector('.booking-list > li')[0].click())

    sleep(1)

    for element in driver.find_elements_by_css_selector('.booking-list > li'):
        if is_after_work(element) and has_available_spot(element):
            print(element.text.split('\n')[0])
            send_message(element.text)

    driver.quit()
    print(f"Done. ({time() - start}s)")

    sleep(60)
