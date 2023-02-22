import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("siti@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("abc") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_b_fail_login_wrong_password(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("siti@gmail.com")
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("password-salah") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_c_fail_login_wrong_email(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("emailsalah@gmail.com") #isi email salah
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("abc") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_d_fail_login_blank_field(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") #email kosong
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # password kosong
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_e_fail_login_blank_password(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("siti@gmail.com")
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # password kosong
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
    
    def test_f_fail_login_blank_email(self):
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("")
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("abc") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()