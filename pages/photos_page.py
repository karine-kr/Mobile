from selenium.webdriver.common.by import By
from pages.base_page import PaginaBase

class PaginaPhotos(PaginaBase):
   LOCATOR_PHOTOS = (By.XPATH, "//android.widget.TextView[@text='Photos']")
   def selecionar_photos(self):
       self.clicar_elemento(self.LOCATOR_PHOTOS)