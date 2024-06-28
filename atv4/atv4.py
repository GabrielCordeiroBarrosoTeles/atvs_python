'''
GRUPO 3

🚀 [Desafio 004] Consumo de API e Envio de Arquivos por E-mail

O objetivo deste desafio, é criar um script Python que se conecte a uma API, obtenha a listagem de todos os usuários, salve os dados retornados em um arquivo e, em seguida, envie esse arquivo por e-mail. Siga as etapas abaixo para completar o desafio:

1.Conexão com API:
    - Utilize a biblioteca requests para realizar a conexão com a API do reqres.
    - Explore as rotas disponíveis na documentação da API para identificar a rota que retorna a listagem de todos os usuários.

2. Obtenção da Listagem de Usuários:
    - Desenvolva uma função que faça uma requisição à rota correspondente para obter a listagem de todos os usuários.
    - Trate a resposta da API para garantir que os dados sejam recuperados com sucesso.

3. Inserção dos Dados em um Arquivo:
    - Após obter a listagem de usuários, crie uma função para inserir esses dados em um arquivo local.
    - O formato do arquivo é de sua escolha (por exemplo, JSON, CSV, TXT, etc.).

4. Envio do Arquivo por E-mail:
    - Utilize uma biblioteca de e-mail para fazer a automação enviar o arquivo por e-mail.

5. Organização do Código:
    - Separe o código em funções distintas, cada uma responsável por uma etapa do processo.
    - A legibilidade e organização do código serão exigidas na avaliação
'''
import os
import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from decouple import config

'''
Cria um arquivo tipo .env  e coloca

GMAIL_USER= seuemail
# Crie e gerencie suas senhas de app           
GMAIL_PASS= senha  

'''

# Carrega as variáveis de ambiente do arquivo .env
gmail_user = config("GMAIL_USER")
gmail_pass = config("GMAIL_PASS")

# URL da API
API_URL = "https://reqres.in/api/users?page=1"


# Função para obter a listagem de todos os usuários
def get_users():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Lança exceção para erros HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao obter usuários da API: {e}")


# Função para salvar os dados em um arquivo JSON
def save_users_to_file(users, filename):
    with open(filename, 'w') as file:
        json.dump(users, file, indent=4)


# Função para enviar o arquivo por e-mail
def send_email_with_attachment(sender_email, receiver_email, subject, body, filename, smtp_server, smtp_port,
                               smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        msg.attach(part)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


# Função principal para executar o script
def main():
    try:
        users = get_users()
        filename = "users.json"
        save_users_to_file(users, filename)

        sender_email = gmail_user
        receiver_email = "email_de_envio"
        subject = "Listagem de Usuários"
        body = "Segue em anexo a listagem de usuários."
        smtp_server = "smtp.gmail.com"
        smtp_port = 465
        smtp_username = gmail_user
        smtp_password = gmail_pass

        send_email_with_attachment(sender_email, receiver_email, subject, body, filename, smtp_server, smtp_port,
                                   smtp_username, smtp_password)
        print("Arquivo enviado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
