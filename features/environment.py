from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# behave hooks
def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def before_scenario(context, scenario):
    context.driver.maximize_window()


def before_step(context, step):
    context.driver.implicitly_wait(5)

def after_all(context):
    context.driver.close()
