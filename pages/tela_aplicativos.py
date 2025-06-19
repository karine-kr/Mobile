from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import logging

class TelaAplicativosPage(BasePage):

    BOTAO_PESQUISSA = (By.ID, "com.android.settings:id/search_app_list_menu")

    CAMPO_BUSCAA = (By.ID, "com.android.settings:id/search_src_text")

    RESULTADO_APLICATIVOSS = (By.XPATH, "//android.widget.TextView[@content-desc='Appium Settings']")

    def buscar_app(self, nome_app: str):

        logging.info("🔍 Buscando app " + nome_app + " na tela de aplicativos")

        self.clicar_elemento(self.BOTAO_PESQUISSA)

        self.digitar_texto(self.CAMPO_BUSCAA, nome_app)

        self.clicar_elemento(self.RESULTADO_APLICATIVOSS)
