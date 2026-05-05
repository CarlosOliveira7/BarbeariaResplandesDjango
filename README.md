# Barbearia Resplandes

Sistema de gerenciamento para barbearia, desenvolvido com foco em **modularidade e integração de múltiplos paradigmas de programação**.

---

## Objetivo:

Este projeto tem como objetivo implementar as funcionalidades centrais de agendamento e controle financeiro em um sistema de barbearia, utilizando boas práticas de desenvolvimento, separação de responsabilidades e integração entre diferentes camadas da aplicação.

Além disso, o sistema busca simular um ambiente real de gestão, permitindo o controle de clientes, barbeiros e serviços, bem como a organização de horários de atendimento, evitando conflitos e melhorando a eficiência operacional.

Além disso, o sistema conta com um módulo financeiro, permitindo o controle de receitas, despesas e cálculo automático do saldo líquido, auxiliando na gestão financeira da barbearia.

---
### **Carlos Oliveira Lopes — Tech Lead & Back-End Developer**
* Responsável pela arquitetura e desenvolvimento do Back-End
* Modelagem do banco de dados e regras de negócio
* Condução de entrevistas e levantamento de requisitos com o cliente

### **Andrei Pereira Lima — Front-End Developer**

* Desenvolvimento da interface visual do módulo de clientes
* Implementação do layout e estilização das telas

---

### **Priscila Ferreira Dias Santos — Front-End Developer**

* Desenvolvimento da interface visual do módulo de agendamento
* Estruturação e estilização das telas

---

### **Ywd Rhavell Ferreira Carvalho — Front-End Developer**

* Desenvolvimento da interface visual do dashboard
* Criação e organização dos componentes visuais



## Tecnologias Utilizadas

- Python + Django
- MySQL
- Tailwind CSS
- Node.js

Certifique-se de ter essas tecnologias devidamente instaladas e configuradas em seu computador

---

## Como rodar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/CarlosOliveira7/BarbeariaResplandesDjango
cd BarbeariaResplandesDjango
```

---

### 2. Criar e ativar ambiente virtual

Crie o ambiente virtual com o comando:

```bash
python -m venv venv
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
.\venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

Caso não exista:

```bash
pip freeze > requirements.txt
```

---

### 4. Variáveis de ambiente

Crie um arquivo `.env` na raiz:

```env
DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=3306

DEBUG=True
```

---

### 5. Banco de dados

Crie o banco no MySQL via terminal ou no seu MySql Workbench:

```sql
CREATE DATABASE nome_do_banco;
```

Depois execute os comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Instalação e Inicialização do Tailwind CSS ( Front-End da Aplicação)

Certifique-se de abrir um outro terminal para rodar o tailwind e um unicamente para o servidor django

```bash
python manage.py tailwind install
python manage.py tailwind start
```

---

### 7. Rodar o servidor ( Back-End da Aplicação )

```bash
python manage.py runserver
```

Acesse para visualizar e utilizar a aplicação:

http://127.0.0.1:8000/

---

## Estrutura do Projeto

```bash
clientes/     → Gestão de clientes
barbeiros/    → Gestão da equipe
theme/        → Tailwind + UI
templates/    → HTML base
media/        → Uploads (ignorado no git)
financeiro/   → Controle de receitas e despesas
```

---

## Organização dos Apps

Todos os apps do sistema seguem o mesmo padrão de organização baseado na arquitetura do Django, utilizando models, views, urls e templates.

Como todos seguem essa mesma estrutura e lógica de funcionamento, será apresentado apenas um exemplo para demonstrar como o sistema funciona na prática.

### Exemplo: App Clientes

O app de clientes foi desenvolvido seguindo o padrão CRUD (Create, Read, Update e Delete), sendo responsável pelo gerenciamento dos dados dos clientes.

#### Model

O model define a estrutura da entidade Cliente no banco de dados, contendo os campos nome, telefone e email. Cada cliente é representado como um objeto da aplicação.

#### Views

As views utilizam classes genéricas do Django para implementar as funcionalidades principais:

- Listagem de clientes  
- Cadastro de novos clientes  
- Edição de clientes  
- Exclusão de clientes  

Também é utilizado controle de acesso com autenticação, garantindo que apenas usuários logados possam utilizar o sistema.

#### URLs

As rotas são responsáveis por conectar as funcionalidades às páginas do sistema, permitindo acessar listagem, cadastro, edição e exclusão de clientes.

#### Templates

Os templates são responsáveis pela interface visual, permitindo a interação do usuário com o sistema, incluindo formulários, listagens e validações.

### Padronização

Os demais apps do sistema, como barbeiros, serviços, agendamentos e financeiro, seguem exatamente essa mesma estrutura e lógica de funcionamento.

Essa padronização garante:

- Organização do código  
- Facilidade de manutenção  
- Reutilização de componentes  
- Escalabilidade do sistema  

---

## Arquitetura e Paradigmas

O projeto foi estruturado utilizando:

- **Programação Orientada a Objetos (POO)** → Models e lógica do Django
- **Programação Funcional** → Funções utilitárias e manipulação de dados
- **Arquitetura em Camadas** → Separação entre:
    
    - Apresentação (templates)
    - Negócio (views/services)
    - Persistência (models)

### Explicação Técnica

A **Programação Orientada a Objetos (POO)** é aplicada principalmente nos models do Django, onde cada entidade do sistema, como Cliente, Barbeiro e Serviço, é representada como uma classe. Isso permite encapsulamento dos dados, reutilização de código e melhor organização das regras de negócio.

A **Programação Funcional** é utilizada em funções auxiliares e validações, contribuindo para um código mais simples, reutilizável e com menor acoplamento.

A **Arquitetura em Camadas** organiza o sistema em:

- Apresentação: interface com o usuário (templates HTML)
- Negócio: regras do sistema (views e services)
- Persistência: comunicação com o banco de dados (models)

Os paradigmas são utilizados de forma integrada, onde a POO estrutura o sistema, a programação funcional auxilia no processamento de dados e a arquitetura em camadas organiza o fluxo da aplicação.

O módulo financeiro segue a mesma estrutura, utilizando models para armazenar receitas e despesas, views para processamento dos dados e templates para exibição das informações, incluindo cálculos automáticos de saldo.

Essa abordagem garante:

- Escalabilidade
- Manutenção facilitada
- Reutilização de código

---

## Roadmap de Desenvolvimento

### Fase 1 - Configuração inicial
-  Criar projeto Django
-  Configurar ambiente virtual
-  Configurar MySQL
-  Criar apps (clientes, barbeiros,serviços)

---

###  Fase 2 - Funcionalidades básicas
- CRUD de clientes
- CRUD de barbeiros
- CRUD de serviços
- Validação de dados

---

### Fase 3 - Regras de negócio

- Sistema de agendamento
- Evitar conflitos de horário
- Controle financeiro com registro de receitas e despesas

O sistema de agendamento foi planejado para garantir que um barbeiro não possa atender dois clientes no mesmo horário, realizando validações antes da confirmação do agendamento.

O módulo financeiro permite registrar entradas e saídas de valores, além de calcular automaticamente o saldo disponível, auxiliando na tomada de decisões.

---

###  Fase 4 - Interface
- Implementar templates HTML
- Estilização com Tailwind
- Responsividade

---

###  Fase 5 - Funcionalidades avançadas
- Dashboard administrativo
- Autenticação de usuários

---

### Fase 6 - Finalização
Testes
Ajustes finais

---

## Considerações Finais

Este projeto demonstra a aplicação prática dos conceitos estudados durante a disciplina, integrando tecnologias modernas e diferentes paradigmas de programação para a construção de um sistema realista de gerenciamento.

Além disso, evidencia a importância da organização do código, da separação de responsabilidades e da documentação clara para o desenvolvimento de software de qualidade.


---
---

