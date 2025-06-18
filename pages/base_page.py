import logging

logging.basicConfig(filename='logs/execucao.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class PaginaBase:
   def __init__(self, driver):
       self.driver = driver
   def clicar_elemento(self, locator):
       logging.info(f"Clicando no elemento: {locator}")
       self.driver.find_element(*locator).click()
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