from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import json

# Create your tests here.
class SeleniumTests(LiveServerTestCase):

   @classmethod
   def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #cls.driver.implicitly_wait(10)

   """    def get_network_responses(self):
        logs = self.driver.get_log("performance")
        network_responses = []
        caps = DesiredCapabilities.CHROME
        caps["goog:loggingPrefs"] = {"performance": "ALL"}
        for log in logs:
            message = json.loads(log["message"])["message"]
            if "Network.responseReceived" in message["method"]:
                network_responses.append(message["params"]["response"])
        return network_responses """

   def testCRUDOperation(self):
       #driver = webdriver.Chrome()
       driver = self.driver
       driver.get('http://localhost:8000/')
       #assert "Hello, world!" in driver.title
       #self.assertIn("Hello, world!", driver.title)
       driver.execute_script("document.title = 'Hello, world!'")
       #username_field = driver.find_element_by_name('username')
       #password_field = driver.find_element_by_name('password')
       username_field = driver.find_element(By.ID, "id_username")
       password_field = driver.find_element(By.ID, "id_password")

       username_field.send_keys('ssahu')
       password_field.send_keys('123')

       #driver.find_element(By.CSS_SELECTOR, "form button[type='submit']").click()

       '''
       submit_button = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.CSS_SELECTOR, "form button[type='submit']"))
       )
       '''

       #submit = driver.find_element(By.ID, "submit")

       #submit_button = driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']")

       #submit_button = driver.find_element_by_css_selector("input[type='submit'][value='Log in']")

       submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Log in']")

       submit_button.click()

       # Capture the redirect URL
       redirect_url = driver.current_url

       # Verify the redirect URL
       #self.assertIn("/mainpage", redirect_url.lower())

       #driver.find_element(By.ID, "name1").send_keys('Morning Run')

       #WebDriverWait(driver, 10)

       #driver.find_element(By.ID, "name1").send_keys('Morning Run')

       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name1"))).send_keys('Morning Run')

       #driver.find_element(By.ID, "date1").send_keys('30/05/2024')

       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "date1"))).send_keys('30/05/2024')

       #driver.find_element(By.ID, "startTime1").send_keys("12:30")
       #driver.find_element(By.ID, "amountOfTime1").send_keys("04:00")
       #driver.find_element(By.ID, "descriptionOfTheTask1").send_keys("Early morning run in the streets")
       #driver.find_element(By.ID, "image").send_keys(os.path.abspath(
                                                             #os.path.join(os.path.dirname(__file__), "..", "1000_F_601654907_FgISykN0GQp39MfRAlgg3IBmLDVIZYYk.jpg")))

       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "startTime1"))).send_keys('12:30')
       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "amountOfTime1"))).send_keys('04:00')
       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "descriptionOfTheTask1"))).send_keys('Early morning run in the streets')
       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "image"))).send_keys(os.path.abspath(
                                                             os.path.join(os.path.dirname(__file__), "..", "1000_F_601654907_FgISykN0GQp39MfRAlgg3IBmLDVIZYYk.jpg")))

       #submit_button_to_add = driver.find_element(By.CSS_SELECTOR, "button[data-v-389b3d8a][type='submit']")

       submit_button_to_add = driver.find_element(By.XPATH, '//button[normalize-space()="Submit"]')

       #submit_button_to_add.click()

       driver.execute_script("arguments[0].click();", submit_button_to_add)
       """
       # Check network responses
       responses = self.get_network_responses()
       for response in responses:
          print(f"URL: {response['url']}, Status: {response['status']}") """

       #retrieve_button = driver.find_element(By.CSS_SELECTOR, "button[value='Fetch all the task details at all the dates']")

       #driver.execute_script("arguments[0].click();", retrieve_button)

       retrieve_button = driver.find_element(By.XPATH, '//button[normalize-space()="Fetch the tasks"]')

       #retrieve_button.click()

       driver.execute_script("arguments[0].click();", retrieve_button)

       #update_button = driver.find_element(By.XPATH, "//button[normalize-space()='Update']")

       update_button = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Update']"))
       )

       driver.execute_script("arguments[0].click();", update_button)

       #driver.find_element(By.ID, "name1").send_keys("Swimming")

       #driver.find_element(By.ID, "date1").send_keys("01/06/2024")

       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name1"))).send_keys("Swimming")
       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "date1"))).send_keys("01/06/2024")

       #driver.find_element(By.ID, "startTime1").send_keys("16:30")

       #driver.find_element(By.ID, "amountOfTime1").send_keys("03:00")

       #driver.find_element(By.ID, "descriptionOfTheTask1").send_keys("3 hours swimming at the sport centre")

       #driver.find_element(By.ID, "image").send_keys(os.path.abspath(
       #                                                      os.path.join(os.path.dirname(__file__), "..", "photo-1622629797619-c100e3e67e2e.avif")))

       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "startTime1"))).send_keys("16:30")
       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "amountOfTime1"))).send_keys("03:00")
       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "descriptionOfTheTask1"))).send_keys("3 hours swimming at the sport centre")
       WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "image"))).send_keys(os.path.abspath(
                                                             os.path.join(os.path.dirname(__file__), "..", "photo-1622629797619-c100e3e67e2e.avif")))

       #submit_button_to_add = driver.find_element(By.CSS_SELECTOR, "button[data-v-3ee9e199][type='submit']")

       submit_button_to_update = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Submit"]'))
       )

       driver.execute_script("arguments[0].click();", submit_button_to_update)

       retrieve_button = WebDriverWait(driver, 10).until(
          EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Fetch the tasks"]'))
       )

       #retrieve_button.click()

       driver.execute_script("arguments[0].click();", retrieve_button)

       #delete_button = driver.find_element(By.XPATH, "//button[@class='text-danger' and @style='color: red;' and text()='Delete']")

       delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Delete']"))
       )

       driver.execute_script("arguments[0].click();", delete_button)

       #calorie_tracker_button = driver.find_element(By.XPATH, '//button[normalize-space()="Calorie Tracker"]')

       #driver.execute_script("arguments[0].click();", calorie_tracker_button)

   def testCalorieTrackerOperation(self):
       driver = self.driver
       driver.get('http://localhost:5173/mainpage/CalorieTracker')

       driver.find_element(By.ID, "query").send_keys('pasta')

       driver.find_element(By.ID, "amountOfCalories").send_keys("12000")

       driver.find_element(By.ID, "dietType").send_keys("high-fiber")

       driver.find_element(By.ID, "mealType").send_keys("lunch")

       submit_button_for_the_diet_plan = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

       driver.execute_script("arguments[0].click();", submit_button_for_the_diet_plan)

       driver.find_element(By.ID, "listOfFoodItems").send_keys("1 packet of cookies")

       retrieve_button = driver.find_element(By.XPATH, '//button[normalize-space()="Fetch the amount of calories intaken"]')

       driver.execute_script("arguments[0].click();", retrieve_button)

       calorie_history_button = driver.find_element(By.XPATH, '//button[normalize-space()="See your Calorie History"]')

       driver.execute_script("arguments[0].click();", calorie_history_button)

       #fetch_calorie_history = driver.find_element(By.XPATH, '//button[normalize-space()="Fetch all the calorie consumption details at all the dates"]')

       fetch_calorie_history = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Fetch all the calorie consumption details at all the dates"]'))
       )

       driver.execute_script("arguments[0].click();", fetch_calorie_history)

   def testExercising_videos(self):

       driver = self.driver
       driver.get('http://localhost:5173/mainpage/FetchingExercisingVideos')

       driver.find_element(By.ID, "queryForVideos").send_keys("30 minutes run")

       submit_button_exercising_videos = driver.find_element(By.XPATH, '//button[normalize-space()="Fetch videos"]')

       driver.execute_script("arguments[0].click();", submit_button_exercising_videos)

       driver.quit()
