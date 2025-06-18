from behave import given, when, then
from pages.configuracoes_page import PaginaConfiguracoes
from pages.photos_page import PaginaPhotos
from pages.permissoes_page import PaginaPermissoes
@given("que estou visualizando o app Photos nas Configurações")
def step_impl(context):
   context.pagina_configuracoes = PaginaConfiguracoes(context.driver)
   context.pagina_configuracoes.acessar_apps()
   context.pagina_configuracoes.ver_todos_os_apps()
   context.pagina_photos = PaginaPhotos(context.driver)
   context.pagina_photos.selecionar_photos()
@when("acesso as permissões de Fotos e Vídeos")
def step_impl(context):
   context.pagina_permissoes = PaginaPermissoes(context.driver)
   context.pagina_permissoes.acessar_permissoes()
   context.pagina_permissoes.acessar_fotos_videos()
@when("seleciono a opção 'Allow'")
def step_impl(context):
   context.pagina_permissoes.permitir()
@when("seleciono a opção 'Don't allow' em Fotos")
def step_impl(context):
   context.pagina_permissoes.nao_permitir()
@then("a opção 'Allow' deve estar marcada")
def step_impl(context):
   assert context.pagina_permissoes.validar_radio_marcado(context.pagina_permissoes.LOCATOR_PERMITIR)
@then("a opção 'Don't allow' deve estar marcada para Fotos")
def step_impl(context):
   assert context.pagina_permissoes.validar_radio_marcado(context.pagina_permissoes.LOCATOR_NAO_PERMITIR)