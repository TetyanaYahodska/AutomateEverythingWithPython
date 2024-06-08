# #from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time


# def get_driver():
#   options = webdriver.ChromeOptions()
#   options.add_argument("disable-infobars")
#   options.add_argument("start-maximized")
#   options.add_argument("disable-dev-shm-usage")
#   options.add_argument("no-sandbox")
#   options.add_experimental_option("excludeSwitches", ["enable-automation"])
#   options.add_argument("disable-blink-features=AutomationControlled")
#   driver = webdriver.Chrome(options=options)
#   driver.get("https://automated.pythonanywhere.com/")
#   return driver

# def clean_text(text):
#   """Extract only the temperature from text"""
#   output = float(text.split(": ")[1])
#   return output

# def write_file(text):
#   """Write input text into a text file"""
#   filename = f"{time.strftime('%Y-%m-%d.%H-%M-%S')}.txt"
#   with open(filename, 'w') as file:
#     file.write(text)
  
# def main():
#   driver = get_driver()
#   while True:
#     time.sleep(2)
#     element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
#     text = str(clean_text(element.text))
#     write_file(text)

# print(main())




from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  print(url)
  response = requests.get(url)
  content = response.text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])
  return rate

print(get_currency('EUR','USD'))