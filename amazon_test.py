import time
import unittest
from appium import webdriver
from amazon_app import AmazonApp
import xmlrunner
appium_server_url = 'http://localhost:4723'
app_path = "apk/amazon.apk"

class TestAmazonApp(unittest.TestCase):
    def setUp(self) -> None:
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Android Emulator',
            app=app_path,
            appPackage="com.amazon.mShop.android.shopping",
            appActivity="com.amazon.mShop.home.HomeActivity",
            language='en',
            locale='US'
        )
        self.driver = webdriver.Remote(appium_server_url, capabilities)
        self.app = AmazonApp(self.driver)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()



    def test_total_number_for_category(self):
        self.app.allow_permissions()
        self.app.skip_sign_in()
        self.app.click_cart_icon()
        self.app.click_home()
        self.app.click_burger_menu()
        self.app.click_shop_by_department()
        time.sleep(5)
        self.app.click_electronics_category()
        self.app.assert_page()

        # Wait for a moment to see the results
        time.sleep(5)
        self.app.click_home()
    def test_add_to_cart(self) -> None:
        self.app.allow_permissions()
        self.app.skip_sign_in()
        self.app.search_bar()
        self.app.click_on_img()
        self.app.assert_price()
        self.app.assert_payment_method()
        self.app.add_cart()
        self.app.assert_add_to_cart()


    def test_filter_by_department(self):
        self.app.allow_permissions()
        self.app.skip_sign_in()
        self.app.click_deal_promotion()
        self.app.click_filters()
        # Wait for a moment to see the results
        time.sleep(5)

    def test_currency_change(self):
        self.app.allow_permissions()
        self.app.skip_sign_in()
        self.app.click_cart_icon()
        self.app.click_home()
        self.app.click_burger_menu()
        self.app.click_settings()
        self.app.click_currency()






if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='report'))
