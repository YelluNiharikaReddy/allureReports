from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from allure_commons.types import AttachmentType


class TestOrangeHRM:
    @allure.severity(allure.severity_level.NORMAL)
    def test_logo(self):
        self.driver = webdriver.Chrome("C:\ Users\Dell\Desktop/chrome driver\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        Status = self.driver.find_element(By.XPATH , "//*[@id='app']/div[1]/div/div[1]/div/div[1]/img").is_displayed()
        if Status == True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testloginscreen",
                          attachment_type=AttachmentType.png)
            self.driver.close()
            assert False




    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome("C:\ Users\Dell\Desktop/chrome driver\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME , "username").send_keys("Admin")
        self.driver.find_element(By.NAME , "password").send_keys("admin123")
        self.driver.find_element(By.XPATH , "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        actual_title = self.driver.title
        if actual_title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testloginscreen",
                          attachment_type=AttachmentType.png)
            assert False



    @allure.severity(allure.severity_level.MINOR)
    def test_list(self):
        pytest.skip("skip this test for now its not yet done ")

