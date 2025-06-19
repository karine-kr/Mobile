from selenium.webdriver.common.by import By
from pages.base_page import PaginaBase

class PaginaAppiumSettings(PaginaBase):
   LOCATOR_APPIUM = (By.ID, "Appium Settings")
   def selecionar_appium_settings(self):
       self.clicar_elemento(self.LOCATOR_APPIUM)