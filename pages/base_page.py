import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logging.basicConfig(filename='logs/execucao.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class PaginaBase:
   def __init__(self, driver):
       self.driver = driver
   def clicar_elemento(self, locator: tuple, timeout: int = 10):
       """
       Aguarda até o elemento estar visível e clica.
       """
       logging.info(f"Clicando no elemento: {locator}")
       try:
           elemento = WebDriverWait(self.driver, timeout).until(
               EC.element_to_be_clickable(locator)
           )
           elemento.click()
       except TimeoutException:
           logging.error(f"Elemento {locator} não encontrado ou não clicável.")
           raise
   def esperar_elemento(self, locator: tuple, timeout: int = 10):
       """
       Aguarda até que o elemento esteja visível na tela e o retorna.
       """
       logging.info(f"Aguardando elemento: {locator}")
       try:
           return WebDriverWait(self.driver, timeout).until(
               EC.visibility_of_element_located(locator)
           )
       except TimeoutException:
           logging.error(f"Elemento {locator} não visível após {timeout} segundos.")
           raise
   def digitar_texto(self, locator: tuple, texto: str, timeout: int = 10):
       """
       Aguarda até o campo estar visível e envia o texto.
       """
       logging.info(f"Digitando no campo {locator}: '{texto}'")
       try:
           campo = WebDriverWait(self.driver, timeout).until(
               EC.visibility_of_element_located(locator)
           )
           campo.clear()
           campo.send_keys(texto)
       except TimeoutException:
           logging.error(f"Campo {locator} não disponível para digitação.")
           raise
   def obter_elemento(self, locator):
       logging.info(f"Obtendo elemento: {locator}")
       return self.driver.find_element(*locator)
   def elemento_visivel(self, locator):
       try:
           visivel = self.driver.find_element(*locator).is_displayed()
           logging.info(f"Elemento visível: {locator} -> {visivel}")
           return visivel
       except:
           logging.error(f"Elemento não visível: {locator}")
           return False