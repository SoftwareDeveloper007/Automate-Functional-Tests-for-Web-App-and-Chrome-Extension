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

    def startSteps(self):

        pTxt = "\n-------- Step 'L002' started!!! --------------------------------------------------------------------"
        print(pTxt)

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        ''' 1. Navigate to staging.getkumbu.com '''
        pTxt = "\n1. Navigate to staging.getkumbu.com\n"
        print(pTxt)
        try:
            self.driver.get(self.url)
            pTxt = "\t\t(Success)\tLoad webpage successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to load webpage"
            print(pTxt)
            self.driver.quit()
            return

        ''' 2. Input email adress: kumbutest@mailinator.com '''
        pTxt = "\n2. Input email adress: kumbutest@mailinator.com\n"
        print(pTxt)

        try:
            inputs = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.kumbu-input"))
            )
        except:
            pTxt = "\t\t(Error)\tCan't find 'Email' and 'Password' Inputs"
            print(pTxt)
            self.driver.quit()
            return

        try:
            email_input = inputs[0]
            email_input.send_keys(self.email)
            pTxt = "\t\t(Success)\tInput email successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to input 'email'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 3. Input password: “kumbu is cool” '''
        pTxt = "\n3. Input password: 'kumbu is cool'\n"
        print(pTxt)

        try:
            pwd_input = inputs[1]
            pwd_input.send_keys(self.password)
            pTxt = "\t\t(Success)\tInputted 'Password' successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to input 'Password'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 4. Click Sign in '''
        pTxt = "\n4. Click Sign in\n"
        print(pTxt)
        try:
            submit_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input#login-submit"))
            )
            submit_btn.click()
            pTxt = "\t\t(Success)\tClicked 'Sign in' button. Logged in successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to click 'Sign in' button"
            print(pTxt)
            self.driver.quit()
            return

        ''' 5. Verify that 'Invalid email or password' displayed '''
        pTxt = "\n5. Verify that 'Invalid email or password' displayed\n"
        print(pTxt)
        try:
            flash_msg = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div#flash-messages"))
            )

            if "Invalid email or password" in flash_msg.text.strip():
                pTxt = "\t\t(Success)\t'Invalid email or password' is displayed"
                print(pTxt)
            else:
                pTxt = "\t\t(Failure)\t'Invalid email or password' is not displayed"
                print(pTxt)
                self.driver.quit()
                return
        except:
            pTxt = "\t\t(Error)\t'Invalid email or password' is not displayed"
            print(pTxt)
            self.driver.quit()
            return

        ''' 6. Click on 'x' to dismiss message '''
        pTxt = "\n6. Click on 'x' to dismiss message\n"
        print(pTxt)

        try:
            x_btn = flash_msg.find_element_by_css_selector("a.close-button")
            x_btn.click()
            pTxt = "\t\t(Success)\tClicked 'x' in 'Invalid email or password' successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to 'x' in 'Invalid email or password'"
            print(pTxt)
            self.driver.quit()
            return

        self.driver.quit()

if __name__ == '__main__':
    app = L002(url='staging.getkumbu.com', email='kumbutest@mailinator.com', password='kumbu is not cool')
    app.startSteps()
