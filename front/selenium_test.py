from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

c = "streamlit-expanderHeader st-ae st-ch st-ag st-ah st-ai st-aj st-co st-bp st-dj st-dk st-dl st-dm st-dn st-ar st-as st-b6 st-b5 st-b3 st-bt st-ca st-cb st-b4 st-cf st-c3 st-c5 st-c4 st-c2"

# Create a new instance of the Chrome driver
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# Navigate to the Streamlit app URL
driver.get("http://localhost:8501/")

predict_tab = []
while(predict_tab == []):
    print("Searching for the predict tab...")
    predict_tab = driver.find_elements(by=By.ID,value="tabs-bui2-tab-1")
    time.sleep(1)
predict_tab = predict_tab[0]
predict_tab.click()
print("Predict tab found and clicked!")

title = None
while(title == None):
    print("Searching for the title input...")
    title = driver.find_element(by=By.CSS_SELECTOR, value="input[aria-label='predict_Title']")
    time.sleep(1)
print("Title input found!")

description = None
while(description == None):
    print("Searching for the description input...")
    description = driver.find_element(by=By.CSS_SELECTOR, value="textarea[aria-label='predict_Description']")
    time.sleep(1)
print("Description input found!")

title.send_keys("Crazy Anime")
description.send_keys("A young student, light yagami, is handed a notebook that gives him super saiyan powers, by a little electric yellow creature. He then uses it to go find the one piece to protect his city again the the Attack Titan.")

pred_button = None
while(pred_button == None):
    print("Searching for the predict button...")
    pred_button = driver.find_element(by=By.CSS_SELECTOR, value="button[class='css-5uatcg edgvbvh10']")
    time.sleep(1)
#pred_button.click()
print("Predict button found and clicked!")
print("Test finished!")
