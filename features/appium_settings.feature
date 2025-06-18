Feature: Permissões do Appium Settings
Scenario: Permitir Localização o tempo todo
 Given que estou na tela inicial de Configurações
 When navego até as permissões de Localização do Appium Settings
 And seleciono a opção 'Permitir o tempo todo'
 Then a opção 'Permitir o tempo todo' deve estar marcada
 
Scenario: Negar permissão de Localização
 Given que estou na tela inicial de Configurações
 When navego até as permissões de Localização do Appium Settings
 And seleciono a opção 'Don't allow' em Localização
 Then a opção 'Don't allow' deve estar marcada