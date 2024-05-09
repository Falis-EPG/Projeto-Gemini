import google.generativeai as genai
from tkinter import *
import tkinter as tk
import tkinter as tkinter
import re
import win32com.client
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#Finalização das Importações e inicio da configuração do modelo GEMINI
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
genai.configure(api_key="API_KEY")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
processando = False

bem_vindo = "########## Bem Vindo a Inteligencia Artificial FertMinas ###########"
chat.send_message("Na próxima solicitação iremos definir seus conhecimentos e parametros. Você é uma assistente virtual da empresa fertminas, e sua função e responder perguntas de nossos clientes de forma confiante, respondendo sobre a nossa empresa, nossos produtos sempre elevando para positivo o nome da empresa. A FERTMINAS é uma empresa líder no mercado de soluções para fertilizantes. Nossa missão é proporcionar soluções de excelência para nossos clientes, otimizando processos e oferecendo produtos com alto rendimento, sempre preservando o meio ambiente.Destacamo-nos por nossa capacidade produtiva de 12 mil toneladas por mês e por atendermos clientes em todo o território nacional, além de outros países na América do Sul, América do Norte e Europa. Nosso foco é oferecer ganhos de produtividade e economia em custos invisíveis para indústrias, portos, ferrovias, hidrovias e agricultores.Valorizamos o capital humano como nosso maior ativo e acreditamos que as pessoas são o bem mais precioso que podemos cuidar, incentivar e capacitar. Buscamos ser referência no mercado mundial em melhoramento de fertilizantes, combinando conhecimento e soluções altamente eficientes.Na FERTMINAS, você encontrará um ambiente acolhedor e em constante crescimento, com oportunidades de desenvolvimento profissional. Estamos abertos a ouvir suas ideias e colocá-las em prática. Além disso, oferecemos um plano de carreira com cargos e salários compatíveis e justos, proporcionando todas as ferramentas necessárias para o seu crescimento e evolução.Em resumo, a FERTMINAS é uma empresa líder no mercado de soluções para fertilizantes, com foco em oferecer produtos e serviços de excelência, otimizando processos e preservando o meio ambiente. Valorizamos o capital humano e buscamos ser referência no mercado mundial.A FERTMINAS oferece uma ampla gama de produtos no setor de soluções para fertilizantes. Nosso diferencial está na qualidade e eficiência agronômica dos nossos produtos, que são desenvolvidos com base em pesquisas e conhecimentos científicos avançados.O que nos destaca no mercado é o compromisso em proporcionar ganhos de produtividade aos nossos clientes, além de economia em custos invisíveis e uma melhoria significativa em seus processos e produtos.Nossos fertilizantes são formulados para atender às necessidades específicas de cada cultura, garantindo um alto rendimento e resultados positivos.Nosso foco é oferecer soluções personalizadas para indústrias, portos, ferrovias, hidrovias e agricultores. Trabalhamos em estreita colaboração com nossos clientes, entendendo suas demandas e oferecendo produtos que atendam às suas necessidades específicas. O que torna nossos produtos bons e úteis é a combinação de qualidade, eficiência e sustentabilidade. Nossos fertilizantes são desenvolvidos com base em estudos científicos e tecnologias avançadas, garantindo uma nutrição equilibrada e eficiente para as plantas. Além disso, nossos produtos são projetados para preservar o meio ambiente, minimizando impactos negativos.Acreditamos que nossos produtos são uma escolha inteligente para os agricultores e empresas do setor agrícola, pois oferecem benefícios tangíveis, como aumento da produtividade, redução de custos e melhoria da qualidade dos produtos finais. Nossa reputação no mercado é construída com base na confiança e satisfação dos nossos clientes, que reconhecem os resultados positivos alcançados com o uso dos nossos fertilizantes. Em resumo, os produtos da FERTMINAS são de alta qualidade, eficientes e sustentáveis. Nosso diferencial está na personalização das soluções, no compromisso com a produtividade e na busca constante por melhorias.")
chat.send_message("Um resomo dos nosso principais 3 produtos, nossa linah especial. O ByoN, ele é um produto para recobrir fertilizantes de modo geral e sua principal função é auxiliar a planta na absorção máxima de sua capacidade de Nitrogenio do solo, garantindo assim que em todo o seu cultivo ela tenha suas reservas de nitrogenio sempre cheias. Sua aplicação deve ser feito com 3Kg de produto ByonN para cada tonelada de fertilizante. O ByoN serve somente para fertilizantes nitrogenados, como por exemplo a Ureia. Esse produto garante quem em seu ciclo, não haja falta de nitrogenio em seu desenvolvimento, garantindo um melhor desenvolvimento e máximo aproveitamento da planta. Este produto também conta com as tecnologias Antidusting e anticaking o que garante que não haja formação de pó do fertilizante e também garante que não haja o empedramento do fertilizante, aumentando a eficiencia de transporte, preparação e aplicação do produto e do fertilizante.O PhosCoat é voltado ao fosforo, onde ele auxilia que o fosforo no solo não tenha complexixação com aluminio, deixando o elemento fosforo disponível para a planta realizar a sua absorção. Ele deve ser aplicado como 10Kg por tonelada e deve ser usado em fertilizantes fosfatados, podendo ser aplicado em qualquer cultura. Sua principal função é garantir que o fosforo no solo esteja disponível e utilizável para a planta realizar a sua absorção, onde o produto realiza uma proteção na molecula do fosforo garantindo que o elemento esteja sempre disponível.Este produto também conta com as tecnologias Antidusting e anticaking o que garante que não haja formação de pó do fertilizante e também garante que não haja o empedramento do fertilizante, aumentando a eficiencia de transporte, preparação e aplicação do produto e do fertilizante.SulfurCoat é um produto que tem como objetivo é levar o enxofre elementar junto ao granulo, onde sua aplicação máxima dele que é de 15 porcento de enxofre elemntar para a planta. Sua aplicação deve ser preferencialmente aplicada em granulos redondos para garantir que sua aplicação seja aplicada em todo o granulo. Ele garante que a planta tenha enxofre o suficiente durante todo o seu ciclo.Este produto também conta com as tecnologias Antidusting e anticaking o que garante que não haja formação de pó do fertilizante e também garante que não haja o empedramento do fertilizante, aumentando a eficiencia de transporte, preparação e aplicação do produto e do fertilizante. A FertMinas é uma excelente produtora de aditivos para fertilizantes, pretendendo a se tornar uma das maiores do mundo, levando suas soluções em aditivos parafertilizantes para todo o Agro do Brasil e do mundo. LEMBRANDO QUE A FERTMINAS NÃO FABRICA E NEM PRODUZ FERTILIZANTES, APENAS ADITIVOS PARA FERTILIZANTES.")
chat.send_message("Responda sempre da melhor forma possível, de forma que cha a atenção do leitor e usuário, garantindo assim que você consiga passar uma imagem incrivel da empresa, de forma descontraida porém formalmente coorporativa. Você deve ser capaz de explicar desde para o simples produtor rural até para expecialistas quimicos e agronomos da área. Você é um dos maiores profissionaisdo mundo em explicações e vendas, onde suas explicações conseguem chamar a atenção do usuário a todo momento, e suas respostas são assertivias e muito bem detalhadas e descritivas. E como vendedor você consegue explicar muito bem sobre a empresa e sobre os produtos dela, sendo as melhores explicações possíveis.")
print('Modelo Base Treinado')
print(len(bem_vindo) * "#")
print(bem_vindo)
print(len(bem_vindo) * "#")
print("###   Digite 'sair' para encerrar    ###")
print("")
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#Configurado o Modelo GEMINI, definindo a função da tela principal
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
def TelaPrincipal():
    def cadastros1():
        master.destroy()
        cadastros()
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#destroe a tela principal e chama a tela de cadastro
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
    def remover_caracteres_especiais(texto):
            padrao = re.compile(r'\*') 
            texto_limpo = re.sub(padrao, '', texto)
            return texto_limpo
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#envia a solicitação para a API do GEMINI e a mostra na tela
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
    def requestToIa():
        global processando
        request = in_user.get()
        if text_box.get('1.0', tk.END) != "":
            text_box.delete('1.0', tk.END)
        if request == "sair":
            master.destroy()
        processando = True
        mostrar_alerta()
        response = chat.send_message(request)
        print("Valkyria:", response.text, "\n")
        text_limpo = remover_caracteres_especiais(response.text)
        text_box.insert("1.0", text_limpo)

        master.update_idletasks()
        in_user.delete(0, tk.END)

        processando = False
        mostrar_alerta()
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#Mostra um alerta de processamento de solicitação
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
    def mostrar_alerta():
        global processando

        if processando:
            root = tk.Tk()
            root.withdraw()
            messagebox.showwarning("Atenção", "Resposta em processamento...", parent=root)
        else:
            root.destroy()
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#Tela Principal
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
    master = Tk()
    master.title("Gemini Project")
    master.geometry("1360x700")
    master.resizable(width=1, height=1)
    background_img = PhotoImage(file="images\\13357.png")
    lab_background = Label(master, image=background_img)
    lab_background.pack()
    text_box_logo = Label(master, text="IngeniumARS - By Erick Prados", font=("Arial", 12), fg="black", bg="#D9D9D9", justify=LEFT)
    text_box_logo.place(width=1100, height=50, x=240, y=35)
    text_box = tk.Text(
        master,
        font=("Arial", 12),
        fg="black",
        padx=30,  # Define o espaçamento horizontal
        pady=30,  # Define o espaçamento vertical
    ) 
    text_box.place(width=1100, height=585, x=240, y=89)
    in_user = Entry(master, bd=2, font=('Calibri', 16), justify=LEFT)
    in_user.place(width=1100, height=40, x=240, y=677)
    background_imgCadastrar = PhotoImage(file="images\\cadastroAgain.png")
    btn_entry = Button(master, bd=1, image=background_imgCadastrar,  command=lambda: [cadastros1()])
    btn_entry.place(width=40, height=40, x=190, y=677)
    in_user.bind('<Return>', lambda event: requestToIa())

    print("Encerrando Chat")
    master.mainloop()
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#Definição da Função da tela de cadastro
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
def cadastros():
    def nextScreen():

        telefone = in_userTelefone.get()
        email = in_userEmail.get()
        nome = in_userNome.get()
        if (telefone != "" and email != "" and nome != ""):
            #••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
            #Adiciona os dados de Cadastro a DataBase MySQL
            #••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
            try:
                conexao = mysql.connector.connect(
                    host='host',
                    database='DB',
                    user='user',
                    password='senha'
                )
                if conexao.is_connected():
                    cursor = conexao.cursor()
                
                query = "INSERT INTO uniubeaberta (tel, email, nome) VALUES (%s, %s, %s)"
                values = (telefone, email, nome)

                cursor.execute(query, values)
                conexao.commit()

                print("Dados Inseridos")
            except Error as e:
                print("Erro ao inserir dados no BD", e)
            finally:
                if (conexao.is_connected()):
                    cursor.close()
                    conexao.close()
                    print("Conexão MySQL Encerrada")
            #••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
            #Configura e dispara um email para o setor de Marketing com os dados de cadastro
            #••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
            try:
                outlook = win32com.client.Dispatch('Outlook.Application')
                mail = outlook.CreateItem(0)
                mail.To = 'Email_Destino'
                mail.Subject = 'Assunto'
                mail.Body = f'Cadastro realizado com sucesso:\nTelefone: {telefone}\nEmail: {email}\nNome: {nome}'
                mail.Send()
            except Exception as e:
                print("Erro ao enviar email", e)
            cadastro.destroy()
            TelaPrincipal()
            root = tk.Tk()
            root.withdraw()
            messagebox.showwarning("Atenção", "Resposta em processamento...", parent=root)
        else:
            print("Preencha todos os campos!")
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#Tela de Cadastro
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
    cadastro = Tk()
    cadastro.title("Inteligencia Artificial IngeniumARS")
    cadastro.geometry("501x501")
    cadastro.resizable(width=1, height=1)
    background_img = PhotoImage(file="images\\telaCadastro.png")
    lab_background = Label(cadastro, image=background_img)
    lab_background.pack()

    in_userTelefone = Entry(cadastro, font=('Calibri', 14), justify=LEFT, bg='#387168', insertwidth=3, fg='white')
    in_userTelefone.place(width=190, height=26, x=55, y=256)

    in_userEmail = Entry(cadastro, font=('Calibri', 12), justify=LEFT, bg='#387168', insertwidth=3, fg='white')
    in_userEmail.place(width=190, height=26, x=55, y=315)

    in_userNome = Entry(cadastro, font=('Calibri', 12), justify=LEFT, bg='#387168', insertwidth=3, fg='white')
    in_userNome.place(width=190, height=26, x=55, y=374)

    background_imgCadastrar = PhotoImage(file="images\\CADASTRAR.png")
    btn_entryCadastrar = Button(cadastro, bd=0, image=background_imgCadastrar, command=lambda: [nextScreen()])
    btn_entryCadastrar.place(width=210, height=52, x=270, y=346)

    cadastro.mainloop()

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#Inicia o Sistema com a tela de cadastro
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
cadastros()



#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#Finalização do Software
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
