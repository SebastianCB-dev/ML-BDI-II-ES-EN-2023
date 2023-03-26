from helpers.platform import get_platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Scraper:
  driver = None

  def __init__(self):
    self.setDriver()
    pass

  def setDriver(self):
    platform = get_platform()
    service = None
    if platform == "Windows":
      service = Service('./drivers/chromedriver.exe')
    elif platform == "Linux":
      service = Service('./drivers/chromedriver')
    elif platform == "Darwin":
      service = Service('./drivers/chromedriver_mac')
    else:
      Exception("No se reconoce el sistema operativo")
    self.driver = webdriver.Chrome(service=service)

  def start(self):
    pass
