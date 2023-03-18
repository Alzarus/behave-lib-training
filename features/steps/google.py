from behave import *
from selenium.webdriver.common.by import By
from time import sleep


@given('we access google website')
def step_impl(context):
    context.driver.get("https://google.com/")


@when('we insert {keywords} to search')
def step_impl(context, keywords):
    context.driver.find_element(By.CLASS_NAME, 'gLFyf').send_keys(
        keywords)


@when('we click on the search button')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'gNO89b').click()


@then('we see the results')
def step_impl(context):
    assert ' 0 ' not in context.driver.find_element(
        By.ID, 'result-stats').get_attribute("textContent")
    # assert context.driver.find_element(
    #     By.CSS_SELECTOR, 'a[class="v-align-middle"][href="/iclinic/bdd-example"]')
    # sleep(5)    # time to see result
