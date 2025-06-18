from selenium.webdriver.common.by import By

from pages.base_page import PaginaBase

class PaginaPermissoes(PaginaBase):

    LOCATOR_PERMISSOES = (By.XPATH, "//android.widget.TextView[@text='Permissoes']")

    LOCATOR_LOCALIZACAO = (By.XPATH, "//android.widget.TextView[@text='Location']")

    LOCATOR_FOTOS_VIDEOS = (By.XPATH, "//android.widget.TextView[@text='Photos and videos']")

    LOCATOR_SEMPRE_PERMITIR = (By.XPATH, "//android.widget.RadioButton[@text='Permitir o tempo todo']")

    LOCATOR_PERMITIR = (By.XPATH, "//android.widget.RadioButton[@text='Allow']")

    LOCATOR_NAO_PERMITIR = (By.XPATH, "//android.widget.RadioButton[@text='Don't allow']")

    def acessar_permissoes(self):

        self.clicar_elemento(self.LOCATOR_PERMISSOES)

    def acessar_localizacao(self):

        self.clicar_elemento(self.LOCATOR_LOCALIZACAO)

    def acessar_fotos_videos(self):

        self.clicar_elemento(self.LOCATOR_FOTOS_VIDEOS)

    def permitir_sempre(self):

        self.clicar_elemento(self.LOCATOR_SEMPRE_PERMITIR)

    def permitir(self):

        self.clicar_elemento(self.LOCATOR_PERMITIR)

    def nao_permitir(self):

        self.clicar_elemento(self.LOCATOR_NAO_PERMITIR)

    def validar_radio_marcado(self, locator):

        radio = self.obter_elemento(locator)

        return radio.get_attribute("checked") == 'true'
 