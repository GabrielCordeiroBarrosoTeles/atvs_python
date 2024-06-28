# [Desafio 004] Consumo de API e Envio de Arquivos por E-mail 🚀

O objetivo deste desafio é criar um script Python que se conecte a uma API, obtenha a listagem de todos os usuários, salve os dados retornados em um arquivo e, em seguida, envie esse arquivo por e-mail. Siga as etapas abaixo para completar o desafio:

1. Conexão com API:
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
    - A legibilidade e organização do código serão exigidas na avaliação.
