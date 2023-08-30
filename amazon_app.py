from appium.webdriver.common.touch_action import TouchAction
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

    def click_settings(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)
        shop_by_department = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Settings']")))
        shop_by_department.click()
        time.sleep(5)

    def click_electronics_category(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)
        electronics_category = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Electronics']")))
        electronics_category.click()

    def assert_page(self):
        wait = WebDriverWait(self.driver,20)
        heading_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Electronics']")))
        expected_heading_text = "Electronics"
        actual_heading_text = heading_element.text
        assert expected_heading_text == actual_heading_text, f"Expected '{expected_heading_text}', but got '{actual_heading_text}'"
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



    def click_currency(self):
        wait = WebDriverWait(self.driver, 20)
        filter_button = wait.until(EC.presence_of_element_located((By.ID, "com.amazon.mShop.android.shopping:id/rs-settings-currency")))
        filter_button.click()
        time.sleep(5)


    def search_bar(self) -> None:
        wait = WebDriverWait(self.driver, 20)
        # Find and tap on the Search bar
        search_bar = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Search Amazon']")))
        search_bar.click()

        # Type "Apple" and press Enter
        search_bar.send_keys("Apple")

        # Wait for search results to load
        time.sleep(5)

    def click_on_img(self) -> None:
        wait = WebDriverWait(self.driver, 20)
        # Find and tap the picture of the product
        product_picture = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Apple iPhone 11, 64GB, White - Unlocked (Renewed Premium)']")))
        product_picture.click()

        time.sleep(5)
        # Swipe Left to Right on the product picture
        start_x = 0.8  # Start from the right side
        end_x = 0.2  # Swipe to the left side
        start_y = end_y = 0.5  # Center of the screen vertically

        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def assert_price(self) -> None:
        wait = WebDriverWait(self.driver, 20)
        # Verify price of the product is displayed
        price_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Price:']")))
        self.assertTrue(price_element.is_displayed())

    def assert_payment_method(self) -> None:
        wait = WebDriverWait(self.driver, 20)
        # Verify payment options are displayed
        payment_options = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Purchase options and add-ons']")))
        self.assertTrue(payment_options.is_displayed())

    def add_cart(self) -> None:
        wait = WebDriverWait(self.driver, 20)
        # Scroll down to find and tap "Add to Cart" button
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Add to Cart']")))
        add_to_cart_button.click()

    def assert_add_to_cart(self) -> None:
        wait = WebDriverWait(self.driver, 20)
        # Verify "Added to Cart" message
        added_to_cart_message = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Added to Cart']")))
        self.assertTrue(added_to_cart_message.is_displayed())