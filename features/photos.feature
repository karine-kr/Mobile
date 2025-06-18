Feature: Permissões do app Photos
Scenario: Permitir acesso a Fotos e Vídeos
 Given que estou visualizando o app Photos nas Configurações
 When acesso as permissões de Fotos e Vídeos
 And seleciono a opção 'Allow'
 Then a opção 'Allow' deve estar marcada
 
Scenario: Negar acesso a Fotos e Vídeos
 Given que estou visualizando o app Photos nas Configurações
 When acesso as permissões de Fotos e Vídeos
 And seleciono a opção 'Don't allow' em Fotos
 Then a opção 'Don't allow' deve estar marcada para Fotos