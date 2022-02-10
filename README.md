# Construção de uma API com Django REST framework

![Lincença do projeto](	https://img.shields.io/github/license/robsonleal/pedroreceitas)
![Bagde status desenvolvimento](https://img.shields.io/static/v1?label=status&message=CONCLUÍDO&color=green)

## Índice

* [Título](#Título)
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)

## Descrição do Projeto

Projeto para construção de uma API que cadastra clientes no banco de dados;

Os valores que podem ser inseridos nos campos estão sendo validados, para garantir a qualidade dos dados que estão sendo armazenados no bando de dados.

## Funcionalidades e Demonstração da Aplicação
- `Funcionalidade 1`: A API deve possui um endpoint para exibir os detalhes de um determinado cliente;
- `Funcionalidade 2`: Aceita requisições do tipo GET, POST, DELETE, PUT, PATCH para a URI /clientes/{id};
- `Funcionalidade 3`: Os dados do cliente são devolvidos no corpo da resposta, no formato JSON.
- `Funcionalidade 4`: Podemos fazer buscar nos clientes, utilizando os campos nome, cpf e se ele é um usuário ativo no sistema;
- `Funcionalidade 5`: Podemos ordenar a exibição dos clientes de forma alfabética, em ordem crescente ou decrescente; 
- `Funcionalidade 6`: Adicionando autenticação básica, para proteger os dados da API de usuários não autorizados;

Listando clientes cadastrados no banco de dados da API:
![Screenshot_20220209_205454](https://user-images.githubusercontent.com/27708175/153311049-a7aa94a8-2916-4b48-872e-b64a3b3ca27d.png)

Exibição dos campos de filtros disponíveis da API:
![Screenshot_20220209_205522](https://user-images.githubusercontent.com/27708175/153311059-7c756bf5-7442-4688-baa2-5753134ecaf5.png)

Endline onde é possivel utilizar as requisições do tipo GET, POST, DELETE, PUT, PATCH para a URI /clientes/{id}:
![Screenshot_20220209_205649](https://user-images.githubusercontent.com/27708175/153311075-f4e66ae6-89a6-42c7-bf19-2d5f35489aa9.png)

## Acesso ao Projeto

Deploy: 
https://limitless-crag-13072.herokuapp.com/clientes/

Autenticação no sistema: <br>
usuário: django <br>
senha: 123789 

- Acesso máquina Local:
```console
git clone git@github.com:robsonleal/django_projeto_clientes.git
cd django-projeto_clientes
python -m venv ./venv
source venv/bin/activate
pip install -r 'requirements.txt'
python manage.py migrate
python manage.py createsuperuser
python populate_script.py
python manage.py runserver
```
- Abrir o endereço localhost:8000 no navegador de sua preferência

## Tecnologias utilizadas
`Django 4`
`Python 3`
