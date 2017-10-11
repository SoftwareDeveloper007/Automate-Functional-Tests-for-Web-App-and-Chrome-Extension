from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

''' Delete Item '''
class C011():
    def __init__(self, url, email, password, collection_txt, img_txt, tag_txt):

        ''' --- Initialize URL, Email, Password --- '''
        self.url = 'https://' + url
        self.email = email
        self.password = password
        self.collection_txt = collection_txt
        self.img_txt = img_txt
        self.tag_txt = tag_txt

    def startSteps(self):

        pTxt = "\n-------- Step 'C011' started!!! --------------------------------------------------------------------"
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

        ''' 5. Click on 'Collection for Test $TEST_NUMBER' '''
        pTxt = "\n5. Click on 'Collection for Test $TEST_NUMBER'\n"
        print(pTxt)
        try:
            collections = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "div.collection.columns.small-12.medium-3.text-center"))
            )
            flag = False
            for collection in collections:
                if self.collection_txt in collection.text.strip():
                    flag = True
                    break

            if flag:
                try:
                    collection.click()
                    pTxt = "\t\t(Success)\tClicked Successfully"
                    print(pTxt)
                except:
                    pTxt = "\t\t(Error)\tFailed to click"
                    print(pTxt)
                    self.driver.quit()
                    return
            else:
                pTxt = "\t\t(Failure)\tFailed to click"
                print(pTxt)
                self.driver.quit()
                return
        except:
            pTxt = "\t\t(Error)\tFailed to click"
            print(pTxt)
            self.driver.quit()
            return

        memory_txt = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "p.collection-meta.item-info"))
        )

        pTxt = "\nNote: '{}' is displayed\n".format(memory_txt.text.strip())
        print(pTxt)

        ''' 6. Click the rightmost menu item '''
        pTxt = "\n6. Click the rightmost menu item\n"
        print(pTxt)

        try:
            dropdown_btns = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "li.is-dropdown-submenu-parent.opens-left"))
            )

            actions = ActionChains(self.driver)
            actions.move_to_element(dropdown_btns[1]).click().perform()
            actions = ActionChains(self.driver)
            actions.move_to_element(dropdown_btns[1]).click().perform()

            #hover = ActionChains(self.driver).move_to_element(dropdown_btns[1])
            #hover.perform()

            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 7. Click Delete Collection '''
        pTxt = "\n7. Click Delete Collection\n"
        print(pTxt)

        try:
            delete_collection_btn = WebDriverWait(dropdown_btns[1], 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.menu.submenu.is-dropdown-submenu.first-sub.vertical > li > a"))
            )
            delete_collection_btn.click()
            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 8. Click Delete Collection '''
        pTxt = "\n8. Click Delete Collection\n"
        print(pTxt)

        try:
            delete_collection_btn = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.collection-delete-options > a"))
            )
            delete_collection_btn.click()
            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        self.driver.quit()
        return

if __name__ == '__main__':
    app = C011(url='staging.getkumbu.com', email='kumbutest@mailinator.com', password='kumbu is cool',
               collection_txt='New Collection', img_txt='Test Image 6', tag_txt='Test Tag 6')
    app.startSteps()
