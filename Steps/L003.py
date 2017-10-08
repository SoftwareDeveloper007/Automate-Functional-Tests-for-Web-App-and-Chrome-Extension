from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class L002():
    def __init__(self, url, email, password):

        ''' --- Initialize URL, Email, Password --- '''
        self.url = 'https://' + url
        self.email = email
        self.password = password

    def startLogin(self):

        pTxt = "\n-------- Step 'L003' started!!! --------------------------------------------------------------------"
        print(pTxt)

        self.driver = webdriver.Chrome()
        # driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver.exe')
        self.driver.maximize_window()

        ''' 1. Navigate to staging.getkumbu.com '''
        pTxt = "\n1. Navigate to staging.getkumbu.com\n"
        print(pTxt)
        try:
            self.driver.get(self.url)
            pTxt = "\t\t(Success)\tLoad webpage successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Failure)\tFailed to load webpage"
            print(pTxt)
            self.driver.quit()
            return

        ''' 2. Click on 'Forgot Password' '''
        pTxt = "\n2. Click on 'Forgot Password'\n"
        print(pTxt)

        try:
            forgot_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span.password-link"))
            )
            forgot_link.click()
            pTxt = "\t\t(Success)\tClicked 'Forgot your password?'"
            print(pTxt)
        except:
            pTxt = "\t\t(Failure)\tCan't click 'Forgot your password?'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 3. Verify that page https://staging.getkumbu.com/reset is displayed '''
        pTxt = "\n3. Verify that page https://staging.getkumbu.com/reset is displayed\n"
        print(pTxt)

        current_url = self.driver.current_url
        if current_url is 'https://staging.getkumbu.com/reset':
            pTxt = "\t\t(Success)\tYou're at 'https://staging.getkumbu.com/reset'"
            print(pTxt)
        else:
            pTxt = "\t\t(Failure)\tYou're at '{}'".format(current_url)
            print(pTxt)

        ''' 4. Input email address : kumbutest@mailinator.com '''
        pTxt = "\n4. Input email address : kumbutest@mailinator.com\n"
        print(pTxt)

        try:
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.kumbu-input"))
            )
            email_input.send_keys(self.email)
            pTxt = "\t\t(Success)\tInput email successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Failure)\tFailed to input 'email'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 5. 'Send' '''
        pTxt = "\n5. 'Send'\n"
        print(pTxt)
        try:
            submit_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input#login-submit"))
            )
            submit_btn.click()
            pTxt = "\t\t(Success)\tClicked 'Send' button."
            print(pTxt)
        except:
            pTxt = "\t\t(Failure)\tFailed to click 'Send' button"
            print(pTxt)
            self.driver.quit()
            return

        ''' 6. Verify that 'An email to reset your password has been sent' is displayed '''
        pTxt = "\n6. Verify that 'An email to reset your password has been sent' is displayed\n"
        print(pTxt)
        try:
            flash_msg = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div#flash-messages"))
            )

            if "An email to reset your password has been sent" in flash_msg.text.strip():
                pTxt = "\t\t(Success)\t'An email to reset your password has been sent' is displayed"
                print(pTxt)
            else:
                pTxt = "\t\t(Failure)\t'An email to reset your password has been sent' is not displayed"
                print(pTxt)
                self.driver.quit()

        except:
            pTxt = "\t\t(Failure)\t'Invalid email or password' is not displayed"
            print(pTxt)
            self.driver.quit()

        ''' 7. Wait 5s '''
        pTxt = "\n6. Wait 5s\n"
        print(pTxt)
        self.driver.implicitly_wait(5)

        ''' 8. Navigate to https://www.mailinator.com/v2/inbox.jsp?zone=public&query=kumbutest# '''
        pTxt = "\n1. Navigate to staging.getkumbu.com\n"
        print(pTxt)
        self.url = "https://www.mailinator.com/v2/inbox.jsp?zone=public&query=kumbutest#"
        try:
            self.driver.get(self.url)
            pTxt = "\t\t(Success)\tLoad a new webpage successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Failure)\tFailed to load a new webpage"
            print(pTxt)
            self.driver.quit()
            return

        ''' 9. Click on 'Reset your Kumbu Password' '''
        pTxt = "\n9. Click on 'Reset your Kumbu Password'\n"
        print(pTxt)

        try:
            reset_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.all_message-min > div.all_message-min_text.all_message-min_text-3"))
            )
            reset_link.click()
            pTxt = "\t\t(Success)\tClicked 'Reset your Kumbu password'"
            print(pTxt)
        except:
            pTxt = "\t\t(Failure)\tCan't Clicked 'Reset your Kumbu password'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 10. Click on 'Reset Password' '''
        pTxt = "\n10. Click on 'Reset Password'\n"
        print(pTxt)

        try:
            reset_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a.mcnButton"))
            )
            reset_link.click()
            pTxt = "\t\t(Success)\tClicked 'Reset your password'"
            print(pTxt)
        except:
            pTxt = "\t\t(Failure)\tCan't Clicked 'Reset your password'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 11. -	In the “New Password” Field, type “kumbu is cool” '''
        pTxt = "\n10. Click on 'Reset Password'\n"
        print(pTxt)

        try:
            reset_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a.mcnButton"))
            )
            reset_link.click()
            pTxt = "\t\t(Success)\tClicked 'Reset your password'"
            print(pTxt)
        except:
            pTxt = "\t\t(Failure)\tCan't Clicked 'Reset your password'"
            print(pTxt)
            self.driver.quit()
            return

if __name__ == '__main__':
    app = L002(url='staging.getkumbu.com', email='kumbutest@mailinator.com', password='kumbu is not cool')
    app.startLogin()
