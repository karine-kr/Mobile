from selenium.webdriver.common.by import By
from pages.base_page import PaginaBase

class PaginaConfiguracoes(PaginaBase):
   LOCATOR_APPS = (By.XPATH, "//android.widget.TextView[@text='Aplicativos']")
   LOCATOR_VER_TODOS = (By.XPATH, "//android.widget.TextView[@text='See all apps']")
   def acessar_apps(self):
       self.clicar_elemento(self.LOCATOR_APPS)
   def ver_todos_os_apps(self):
       self.clicar_elemento(self.LOCATOR_VER_TODOS)