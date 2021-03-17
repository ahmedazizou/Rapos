# -*- coding: utf-8 -*-
import unittest
import time
import os
from selenium import webdriver # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore

class TestUpload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "http://the-internet.herokuapp.com/upload"
        self.path_to_image = f'{os.getcwd()}/img/image.png'
        self.image_file_name = 'image.png'
        self.result = "screen/test.png"
    def test_upload(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(2)
        upload_input = driver.find_element_by_id('file-upload')
        self.assertTrue(upload_input)
        upload_input.send_keys(self.path_to_image)
        time.sleep(2)
        submit_btn = driver.find_element_by_id('file-submit')
        self.assertTrue(submit_btn)
        submit_btn.click()
        time.sleep(2)
        uploaded_file_name = driver.find_element_by_id('uploaded-files').text
        self.assertEqual(uploaded_file_name, self.image_file_name)
        driver.save_screenshot(self.result)
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()
