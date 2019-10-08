from selenium import webdriver


def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(2)


def after_feature(context, feature):
    context.driver.quit()
