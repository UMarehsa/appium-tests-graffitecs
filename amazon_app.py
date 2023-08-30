from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class AmazonApp:
    def __init__(self, driver):
        self.driver = driver

    def allow_permissions(self):
        wait = WebDriverWait(self.driver, 40)
        wait.until(EC.presence_of_element_located((By.ID, 'com.android.permissioncontroller:id/permission_allow_button'))).click()

    def skip_sign_in(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button'))).click()

    def click_cart_icon(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.FrameLayout[@content-desc='Cart 0 item Tab 3 of 4']/android.widget.ImageView"))).click()

    def click_burger_menu(self):
        wait = WebDriverWait(self.driver, 20)
        burger_menu = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Browse menu Tab 4 of 4"]')))
        burger_menu.click()

    def click_shop_by_department(self):
        wait = WebDriverWait(self.driver, 20)
        shop_by_department = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Shop by Department']")))
        shop_by_department.click()

    def click_electronics_category(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)
        electronics_category = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Electronics']")))
        electronics_category.click()

    def click_home(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)
        home_button = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Home Tab 1 of 4']")))
        home_button.click()

    def click_deal_promotion(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)
        deal_button = wait.until(EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Shop deals ']/android.widget.TextView")))
        deal_button.click()

    def click_filters(self):
        wait = WebDriverWait(self.driver, 20)
        filter_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Filters']")))
        filter_button.click()

    def click_see_more(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)
        filter_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='See more']")))
        filter_button.click()

    def click_software(self):
        wait = WebDriverWait(self.driver, 20)
        filter_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Software']")))
        filter_button.click()
