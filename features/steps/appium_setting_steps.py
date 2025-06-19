from behave import given, when, then
from pages.configuracoes_page import PaginaConfiguracoes
from pages.appium_settings_page import PaginaAppiumSettings
from pages.permissoes_page import PaginaPermissoes
@given("que estou na tela inicial de Configurações")
def step_impl(context):
   context.pagina_configuracoes = PaginaConfiguracoes(context.driver)
@when("navego até as permissões de Localização do Appium Settings")
def step_impl(context):
   # context.paginaconfiguracoes.acessar_apps()
   context.pagina_configuracoes.ver_todos_os_apps()
   context.pagina_appium = PaginaAppiumSettings(context.driver)
   context.pagina_appium.selecionar_appium_settings()
   context.pagina_permissoes = PaginaPermissoes(context.driver)
   context.pagina_permissoes.acessar_permissoes()
   context.pagina_permissoes.acessar_localizacao()
@when("seleciono a opção 'Permitir o tempo todo'")
def step_impl(context):
   context.pagina_permissoes.permitir_sempre()
@when("seleciono a opção 'Don't allow' em Localização")
def step_impl(context):
   context.pagina_permissoes.nao_permitir()
@then("a opção 'Permitir o tempo todo' deve estar marcada")
def step_impl(context):
   assert context.pagina_permissoes.validar_radio_marcado(context.pagina_permissoes.LOCATOR_SEMPRE_PERMITIR)
@then("a opção 'Don't allow' deve estar marcada")
def step_impl(context):
   assert context.pagina_permissoes.validar_radio