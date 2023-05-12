# Autenticação usando Session Cookie Token

Este projeto implementa um sistema de autenticação básico usando tokens de sessão. Ele fornece uma estrutura simples para lidar com o registro, login e logout de usuários, além de proteger rotas específicas que exigem autenticação.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3
- pip (Python Package Installer)
- Mongo
- Redis

## Instalação

1. Clone este repositório:

   ```shell
   git clone https://github.com/Lucasal072/session_token_auth
   ```

2. Acesse o diretório do projeto:

   ```shell
   cd session_token_auth
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```shell 
   python3 -m venv env
   source env/bin/activate
   ```

4. Instale as dependencias do projeto
    ```shell
    pip install -r requirements.txt
   ```
## Configuração

1. Acesse a pasta config e edite e edite o arquivo settings.py
   ```shell
   cd config
   vim settings.py
   ```
2. Para configurações do uwsgi edite o arquivo uwsgi.ini
   ```shell
   vim uwsgi.ini
   ```
## Execução
1. Inicie o projeto com o seguinte comando
   ```shell
   uwsgi uwsgi.ini
   ```


## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, por favor, siga as etapas abaixo:

1. Abra uma issue: Se você identificou um problema, tem uma sugestão ou deseja discutir uma nova funcionalidade, abra uma issue descrevendo detalhadamente o que você gostaria de adicionar ou modificar.

2. Faça um fork do repositório: Faça um fork deste repositório para sua própria conta.

3. Crie um branch: Crie um branch para suas alterações no código.

4. Faça suas alterações: Faça as alterações desejadas no código, seguindo as diretrizes de estilo e boas práticas do projeto.

5. Teste suas alterações: Certifique-se de testar suas alterações para garantir que elas não causem problemas ou quebras no projeto.

6. Envie um pull request: Quando estiver satisfeito com suas alterações, envie um pull request. Descreva claramente as alterações realizadas e forneça qualquer contexto necessário.

7. Revisão de código: Suas alterações passarão por uma revisão de código, onde outros colaboradores podem fornecer feedback e sugerir melhorias.

8. Integração: Após a aprovação da revisão de código, suas alterações serão integradas ao projeto principal.

Agradecemos antecipadamente por suas contribuições!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Sinta-se à vontade para utilizar, modificar e distribuir o código conforme necessário.
   
