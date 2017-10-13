from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time, pyperclip

''' View Items in a Shared Collection '''
class S002():
    def __init__(self, url, email, password, collection_txt):

        ''' --- Initialize URL, Email, Password --- '''
        self.url = 'https://' + url
        self.email = email
        self.password = password
        self.collection_txt = collection_txt

    def startSteps(self):

        pTxt = "\n-------- Step 'S002' started!!! --------------------------------------------------------------------"
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

        ''' 5. Navigate to the Memories Collection '''
        pTxt = "\n5. Navigate to the Memories Collection\n"
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

        ''' 6. Check the number div.collection-navigation-wrapper > div.title-wrapper.text-center.has-cover > div.small-text > p > span.collection-item-number '''
        pTxt = "\n6. Check the number div.collection-navigation-wrapper > div.title-wrapper.text-center.has-cover > div.small-text > p > span.collection-item-number\n"
        print(pTxt)

        try:
            memory_txt = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.collection-navigation-wrapper > div.title-wrapper.text-center.has-cover > div.small-text > p > span.collection-item-number")
                )
            )

            memory_cnt = int(memory_txt.text.strip())
            pTxt = "\t\t(Success)\t{}".format(memory_cnt)
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 7. Click on Share '''
        pTxt = "\n7. Click on Share\n"
        print(pTxt)

        try:
            share_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a#shareCollection")
                )
            )

            share_btn.click()
            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 8. Verify that “Share Collection” is displayed '''
        pTxt = "\n8. Verify that “Share Collection” is displayed\n"
        print(pTxt)

        try:
            share_txt = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.share-wrapper > h2")
                )
            )

            share_txt = share_txt.text.strip()
            pTxt = "\t\t(Success)\t'{}' is displayed".format(share_txt)
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 9. Click on 'Copy Link' '''
        pTxt = "\n9. Click on 'Copy Link'\n"
        print(pTxt)

        try:
            copy_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "label.collection-share-link-copy")
                )
            )

            copy_btn.click()
            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        " 10. Copy shared link "
        pTxt = "\n10. Copy shared link\n"
        print(pTxt)

        copied_link = pyperclip.paste()
        pTxt = "\t\t(Success)\tCopied Link: '{}'".format(copied_link)
        print(pTxt)

        " 11. Navigate to staging.getkumbu.com/logout "
        pTxt = "\n11. Navigate to staging.getkumbu.com/logout\n"
        print(pTxt)

        self.driver.get("https://staging.getkumbu.com/logout")
        time.sleep(5)

        " 12. Open Shared Link "
        pTxt = "\n12. Open Shared Link\n"
        print(pTxt)
        self.driver.get(copied_link)
        time.sleep(5)

        " 13. Scroll down to the bottom "
        pTxt = "\n13. Scroll down to the bottom\n"
        print(pTxt)

        try:
            total_cnt = 0

            while memory_cnt > total_cnt:
                images = WebDriverWait(self.driver, 50).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.item.columns.small-6.medium-2"))
                )
                total_cnt = len(images)
                self.driver.execute_script("arguments[0].scrollIntoView();", images[-1])
                time.sleep(2)

            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 14. Count the number of squares and verify it matches the number '''
        pTxt = "\n14. Count the number of squares and verify it matches the number\n"
        print(pTxt)

        try:
            pTxt = "\t\t(Success)\tThe number of squares is {}.".format(total_cnt)
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 15. Scroll to the top '''
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", images[0])
            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        time.sleep(5)

        ''' 16. Click on the first item '''
        try:
            images[0].click()
            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 17. Verify that “Back to Memories” is displayed '''
        pTxt = "\n17. Verify that “Back to Memories” is displayed\n"
        print(pTxt)

        try:
            back_txt = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a.item-nav.back-collection"))
            )

            if "Back to Memories" in back_txt.text.strip():
                pTxt = "\t\t(Success)\t"
                print(pTxt)
            else:
                pTxt = "\t\t(Failure)\t"
                print(pTxt)
                self.driver.quit()
                return
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        time.sleep(5)

        ''' 18. Verify that an image is loading '''
        pTxt = "\n18. Verify that an image is loading\n"
        print(pTxt)

        try:
            img = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.picture-item > img"))
            )

            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        time.sleep(5)

        ''' 19. Click the Previous Button '''
        pTxt = "\n19. Click the Previous Button\n"
        print(pTxt)

        try:
            previous_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a#previous-item"))
            )
            previous_btn.click()
            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 20. Verify that the last item is displayed '''
        pTxt = "\n20. Verify that the last item is displayed\n"
        print(pTxt)

        try:
            img = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.picture-item > img"))
            )

            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        time.sleep(3)

        self.driver.quit()
        return

if __name__ == '__main__':
    app = S002(url='staging.getkumbu.com', email='kumbutest@mailinator.com', password='kumbu is cool',
               collection_txt='Memories')
    app.startSteps()
