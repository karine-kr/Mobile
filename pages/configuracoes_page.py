from selenium.webdriver.common.by import By
from pages.base_page import PaginaBase
import logging

class PaginaConfiguracoes(PaginaBase):
#    LOCATOR_APPS = (By.XPATH, "//android.widget.TextView[contains(@text,'Aplicativos')]")
#    LOCATOR_VER_TODOS = (By.XPATH, "//android.widget.TextView[@text='Ver todos os apps']")
#    def acessar_apps(self):
#        self.clicar_elemento(self.LOCATOR_APPS)
#    def ver_todos_os_apps(self):
#        elemento = self.buscar_texto_com_swipe("Aplicativos")
#        elemento.click()
   LUPA_PESQUISA = (By.XPATH, "//android.widget.Button[@content-desc='Pesquisar nas Configurações']")
   CAMPO_PESQUISA = (By.ID, "com.android.settings.intelligence:id/search_src_text")
   RESULTADO_APLICATIVOS = (By.XPATH, "//android.widget.TextView[contains(@text, 'Aplicativos')]")
   def ver_todos_os_apps(self):
       logging.info("🔍 Acessando menu de aplicativos via busca")
       self.clicar_elemento(self.LUPA_PESQUISA)
       self.digitar_texto(self.CAMPO_PESQUISA, "Aplicativos")
       self.clicar_elemento(self.RESULTADO_APLICATIVOS)