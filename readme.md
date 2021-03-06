## Servidor Amazon Lightsail
Servidor web Linux Ubuntu configurado para a aplicação de catalogo de materiais esportivos.

### Acesso
* Usuário: grader
* Porta SSH: 2200
* IP: 35.170.78.167
* DNS: http://dalamangas.com.br/

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
* Adicionado usuário grader para acesso ao Servidor;
* Adicionado usuário catalog para o banco de dados PostgreSQL;
* Configuração do Uncomplicated Firewall (UFW) para permitir apenas conexões de entrada para SSH (porta 2200), HTTP (porta 80) e NTP (porta 123).

### Pré-requisito do App
* Ter um web browser instalado como o [Google Chrome](https://www.google.com/chrome/?brand=CHBD&gclid=EAIaIQobChMIzNCL26fw3gIVwwaRCh3SlgKnEAAYAiAAEgJpiPD_BwE&gclsrc=aw.ds).

### Utilizando o App
Acesse o aplicativo visitando http://dalamangas.com.br/catalog/, navegue pelos produtos e categorias e caso precise alterar, criar um novo registro ou deletar um item, faça o Login com uma conta do google clicando no botão *Login*.

### API
O aplicativo possui uma API visitando http://dalamangas.com.br/catalog/JSON/.

### Built With
* **[Python](https://www.python.org/)** - *Linguagem de Programação*
* **[Flask](http://flask.pocoo.org/)** - *The Web Framework*
* **[SQL Alchemy](https://www.sqlalchemy.org/)** - *The Python SQL Toolkit and Object Relational Mapper*
* **[HTML](https://developer.mozilla.org/pt-PT/docs/Web/HTML)** - *HyperText Markup Language*
* **[CSS](https://developer.mozilla.org/pt-PT/docs/Web/CSS)** - *Cascading Style Sheets*
* **[PostgreSQL](https://www.postgresql.org/)** - *Database*

### Autor
* **Rodrigo Dalamangas** - *Initial Work*
