Markdown

# 💈 Barbearia System

Sistema de gerenciamento para barbearias desenvolvido com **Django**, **MySQL** e **Tailwind CSS**. 
O projeto conta com módulos de Clientes, Barbeiros e Serviços, utilizando uma interface moderna em Dark Mode.

---

## 🛠️ Pré-requisitos

Antes de começar, você vai precisar ter instalado:
* [Python 3.10+](https://www.python.org/)
* [MySQL Server](https://dev.mysql.com/downloads/installer/)
* [Node.js & NPM](https://nodejs.org/) (necessário para o Tailwind CSS)

---

## 🚀 Como configurar o projeto

Siga os passos abaixo para rodar o projeto localmente:

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio

2. Criar e ativar o Ambiente Virtual (venv)
Bash

# Criar
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

3. Instalar as dependências do Python
Bash

pip install -r requirements.txt

    Nota: Se você ainda não criou o arquivo requirements, gere-o com: pip freeze > requirements.txt

4. Configurar as Variáveis de Ambiente

Crie um arquivo chamado .env na raiz do projeto e adicione suas credenciais do MySQL:
Snippet de código

DB_NAME=nome_do_seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
DEBUG=True
SECRET_KEY=sua_chave_secreta_django

5. Configurar o Banco de Dados

No terminal do MySQL, crie o banco de dados:
SQL

CREATE DATABASE nome_do_seu_banco;

Depois, aplique as migrações do Django:
Bash

python manage.py makemigrations
python manage.py migrate

6. Configurar o Tailwind CSS

Instale as dependências do Node e inicie o compilador do Tailwind:
Bash

python manage.py tailwind install
python manage.py tailwind start

7. Rodar o Servidor

Em um novo terminal (com a venv ativa), execute:
Bash

python manage.py runserver

📁 Estrutura do Projeto

    clientes/: Gestão de cadastros de clientes.

    barbeiros/: Gestão da equipe de barbeiros.

    theme/: App responsável pelo design e Tailwind CSS.

    media/: Armazenamento de imagens de upload (não rastreado pelo Git).

    templates/: Arquivos HTML base do sistema.

🤝 Como contribuir

    Faça um Fork do projeto.

    Crie uma Branch para sua modificação (git checkout -b feature/nova-funcionalidade).

    Faça o Commit das suas alterações (git commit -m 'Adicionando nova funcionalidade').

    Faça o Push para a Branch (git push origin feature/nova-funcionalidade).

    Abra um Pull Request.

📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


---