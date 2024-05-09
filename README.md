# Projeto-Gemini
Projeto prático feito para um evento junto a empresa FertMinas! Consiste em um sistema de coleta de cadastro junto a um chatbot que reponde as perguntas relacionadas a empresa. Excelente projeto para se levar em eventos.


* IMPORTS *

| As Bibliotecas usadas no projeto são:

• google.generativeai as genai
• tkinter as tk
• win32com.client
• mysql.connector
• mysql.connector import Error

••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

O sistema inicia com a configuração da API e do modelo do Gemini, definindo o history=[]

••••••••

Logo Após, o sistema envia 3 mensagens para o modelo Gemini, estas informações que contém dados institucionais da empresa, informações dos produtos, quem a empresa é... então, após enviado esses textos, um print() é executado informando que o projeto foi treinado com sucesso.

••••••••

Ao final do código, é chamado a função "cadastros()", essa função executa o TkInter, gerando uma primeira tela, com campos a serem preenchidos e um botão.

![telaCadastro](https://github.com/Falis-EPG/Projeto-Gemini/assets/106707009/a5bd82d1-f8f5-4ee3-a8f9-94e3576f2257)

O usuário preenche esses dados e clica em cadastrar, o que chama a função "nextScreen()", essa pegaos dados dos campos em que o usuário preencheu, verifica se todos os campos foram preenchidos ou não, e inicia  uma conexão com o banco MySQL usando o "Try:". Ele insere os dados que o usuário preencheu na tabela do MySQL e então fecha a conexão com o MySQL.

Logo em seguida um outro "Try:" é executado, desta vez ele usa a biblioteca win32com.client para usar o aplicativo do outlook da máquina (funciona apenas em máquinas Windows), ele pega os dados que o usuário preencheu e coloca no body do email e então o envia.

Por fim o código destoi essa tela de cadastr e chama a função "TelaPrincipal()", executando a tela do chatbot.

••••••••

![image](https://github.com/Falis-EPG/Projeto-Gemini/assets/106707009/a51ac361-3c00-4faf-9db9-c787ff92d68d)

Essa tela é criada com tres elementos principais, um tk.text (que será onde as respostas do GEMINI aparecerão), um campo Entry (que é onde o usuário pode realizar as solicitações) e um pequeno botão que retorna para a tela de cadastro.

O usuário realiza a solicitação no campo Entry e então clica no Enter do teclado, o que envia a solicitação para o modelo do GEMINI, usando a função "requestToIA()"... um alerta é mostrando mostrando que a resposta está em processamento, utilizando o messagebox do tkinter.

Quando a solicitação estiver pronta, então ela é exibida dentro do objeto tkText, sendo visivel ao usuário.

••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

Este é um projeto real que foi utilizado em um evento universitário a berto a comunidade na cidade de Uberaba, onde fomos convidados a participar.

Para nós o principal objetivo deste evento e coletar novos talentos para futuras contratações e ter uma ferramenta para tirar dúvidas destes universitários. 

Uma segunda versão dete projeto també foi criada para um outro evento que participaremos em janeiro, e o objetivo é ter um totem onde qualquer pessoa do evento possa realizar qualquer pergunta sobre nossos produtos, tirar dúvidas sobre a empresa... Nesta Versão também a uma tela para coleta de dados (Leads), o que será usado pela nossa equipe comercial futuramente.

••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

* Developed By IngeniumARS *
* Developer - FalisEPG - Erick Prados *

••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
