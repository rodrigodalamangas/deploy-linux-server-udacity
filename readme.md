## Servidor Amazon Lightsail
Servidor web Linux Ubuntu configurado para a aplicação de catalogo de materiais esportivos.

### Acesso
* Usuário: grader
* Porta SSH: 2200
* IP: 35.170.78.167

### Softwares Instalados no Servidor
* Python 2.7
* Git
* Apache
* Python mod_wsgi
* PostgreSQL
* bleach==3.0.2
* certifi==2018.10.15
* chardet==3.0.4
* Click==7.0
* Flask==1.0.2
* Flask-HTTPAuth==3.2.4
* Flask-SQLAlchemy==2.3.2
* httplib2==0.11.3
* idna==2.7
* itsdangerous==1.1.0
* Jinja2==2.10
* MarkupSafe==1.1.0
* oauth2client==4.1.3
* packaging==18.0
* passlib==1.7.1
* psycopg2==2.7.5
* psycopg2-binary==2.7.5
* pyasn1==0.4.4
* pyasn1-modules==0.2.2
* pyparsing==2.3.0
* redis==2.10.6
* requests==2.20.0
* rsa==4.0
* six==1.11.0
* SQLAlchemy==1.2.13
* urllib3==1.24.1
* webencodings==0.5.1
* Werkzeug==0.14.1

### Resumo de Configurações
* Adicionado usuário grader para acesso ao Servidor
* Adicionado usuário catalog para o banco de dados PostgreSQL
* Configuração do Uncomplicated Firewall (UFW) para permitir apenas conexões de entrada para SSH (porta 2200), HTTP (porta 80) e NTP (porta 123).

### Pré-requisito do App
* Ter um web browser instalado como o [Chrome](https://www.google.pt/intl/pt-PT/
chrome/?brand=CHBD&gclid=EAIaIQobChMI3Iuek8H32gIVDBGRCh3xvwoQEAAYASAAEgK3MPD_
BwE&gclsrc=aw.ds&dclid=CIDp5pnB99oCFY9HhgodXyAAhw).

### Utilizando o App
Acesse o aplicativo visitando http://35.170.78.167/catalog/ localmente, navegue pelos produtos e categorias e caso precise alterar, criar um novo registro ou deletar um item, faça o Login com uma conta do google clicando no botão *Login*.

### API
O aplicativo possui uma API visitando http://35.170.78.167/catalog/JSON/.

### Built With
* **Python** - *Linguagem de Programação*
* **Flask** - *The Web Framework*
* **SQL Alchemy** - *The Python SQL Toolkit and Object Relational Mapper*
* **HTML** - *HyperText Markup Language*
* **CSS** - *Cascading Style Sheets*
* **PostgreSQL** - *Database*

### Autor
* **Rodrigo Dalamangas** - *Initial Work*
