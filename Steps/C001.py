from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class C001():
    def __init__(self, url, email, password, collection_txt):

        ''' --- Initialize URL, Email, Password --- '''
        self.url = 'https://' + url
        self.email = email
        self.password = password
        self.collection_txt = collection_txt

    def startLogin(self):

        pTxt = "\n-------- Step 'C001' started!!! --------------------------------------------------------------------"
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
            inputs = WebDriverWait(self.driver, 50).until(
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
            submit_btn = WebDriverWait(self.driver, 50).until(
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

        ''' 5. Click on 'New Collection' '''
        pTxt = "\n5. Click on 'New Collection'\n"
        print(pTxt)
        try:
            header = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.top-bar.secondary-navigation"))
            )
            new_collection = header.find_element_by_css_selector("div.top-bar-left > ul.menu > li > a")
            new_collection.click()
            pTxt = "\t\t(Success)\tClicked 'New Collection'"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tCan't click'New Collection'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 6. Click on “New Collection” in the header, and select all text '''
        pTxt = "\n6. Click on “New Collection” in the header, and select all text\n"
        print(pTxt)
        try:
            new_collection = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.title-wrapper.text-center > h1"))
            )

            actionChains = ActionChains(self.driver)
            actionChains.click(new_collection).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL) \
                .send_keys(Keys.DELETE).send_keys(self.collection_txt).perform()

            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 7. Check that it displays 0 memories '''
        pTxt = "\n7. Check that it displays 0 memories\n"
        print(pTxt)
        try:
            display_txt = self.driver.find_element_by_css_selector("p.collection-meta.item-info").text.strip()
            pTxt = "\t\t(Success)\t'{}' is displayed".format(display_txt)
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 8. Click 'Back to collections' '''
        pTxt = "\n8. Click 'Back to collections'\n"
        print(pTxt)
        try:
            back_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.back-collections"))
            )
            back_btn.click()
            pTxt = "\t\t(Success)\t Clicked 'Back to collections'"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t Failed to click 'Back to collections'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 9. Check that 'Collection for Test $TEST_NUMBER' is visible on the page '''
        pTxt = "\n9. Check that 'Collection for Test $TEST_NUMBER' is visible on the page\n"
        print(pTxt)
        try:
            collections = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.collection.columns.small-12.medium-3.text-center"))
            )
            flag = False
            for collection in collections:
                if self.collection_txt in collection.text.strip():
                    flag = True
                    break

            if flag:
                pTxt = "\t\t(Success)\t '{}' is displayed".format(self.collection_txt)
            else:
                pTxt = "\t\t(Failure)\t '{}' is not displayed".format(self.collection_txt)
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t '{}' is not displayed".format(self.collection_txt)
            print(pTxt)
            self.driver.quit()
            return

        self.driver.quit()


if __name__ == '__main__':
    app = C001(url='staging.getkumbu.com', email='kumbutest@mailinator.com', password='kumbu is cool',
               collection_txt='Kumbu Test 6')
    app.startLogin()
