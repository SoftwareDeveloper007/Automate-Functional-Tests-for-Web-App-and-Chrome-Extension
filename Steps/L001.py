from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

''' Correct Login  '''
class L001():
    def __init__(self, url, email, password):

        ''' --- Initialize URL, Email, Password --- '''
        self.url = 'https://' + url
        self.email = email
        self.password = password

    def startSteps(self):

        pTxt = "\n-------- Step 'L001' started!!! --------------------------------------------------------------------"
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

        ''' 5. Verify that username is visible'''
        pTxt = "\n5. Verify that username is visible\n"
        print(pTxt)
        try:
            user_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.profile-link"))
            )
            user_name = user_btn.text.strip()
            pTxt = "\t\t(Success)\tUsername:'{}' is visible".format(user_name)
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tUsername is not visible"
            print(pTxt)
            self.driver.quit()
            return

        ''' 6. Click on username '''
        pTxt = "\n6. Click on username\n"
        print(pTxt)
        try:
            user_btn.click()
            pTxt = "\t\t(Success)\tClicked 'user name : {}'".format(user_name)
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to click 'user name : {}'".format(user_name)
            print(pTxt)
            self.driver.quit()
            return

        ''' 7. Verify that profile panel is visible '''
        pTxt = "\n7. Verify that profile panel is visible\n"
        print(pTxt)
        try:
            signout_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "li.profile-tab-signout > a"))
            )
            pTxt = "\t\t(Success)\tProfile pannel is visible"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tProfile pannel is not visible"
            print(pTxt)
            self.driver.quit()
            return

        ''' 8. Click on Logout '''
        pTxt = "\n8. Click on Logout\n"
        print(pTxt)
        try:
            signout_btn.click()
            pTxt = "\t\t(Success)\tProfile pannel is visible. Clicked 'Sign out'"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tProfile pannel is not visible. And failed to click 'Sign out'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 9.Verify that you are back at staging.getkumbu.com '''
        pTxt = "\n9.Verify that you are back at staging.getkumbu.com\n"
        print(pTxt)
        current_url = self.driver.current_url
        if current_url == 'https://staging.getkumbu.com':
            pTxt = "\t\t(Success)\tyou are back at staging.getkumbu.com"
            print(pTxt)
        else:
            pTxt = "\t\t(Error)\tyou are not back at staging.getkumbu.com"
            print(pTxt)
            self.driver.quit()
            return

        self.driver.quit()

if __name__ == '__main__':
    app = L001(url='staging.getkumbu.com', email='kumbutest@mailinator.com', password='kumbu is cool')
    app.startSteps()
