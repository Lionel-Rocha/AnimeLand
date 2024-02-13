# AnimeLand ⛩️

## E-commerce de produtos de anime em Django 🐍

Esse é um projeto de estudo, disponível gratuitamente para clone ou download. Para rodar, basta fazer o download do que está no requirements.txt ou simplesmente copiar o repositório e colar no serviço de deploy à sua escolha. 

### Rodar localhost com Python
Para ver o resultado no localhost, você precisa de *python*. Depois, é só entrar na pasta do projeto e seguir os passos:
1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver

E pronto!

### Rodar via Docker
Você vai ver o resultado em localhost, mas não necessitará de python.
1. docker build -t *nome-da-sua-imagem* .
2. docker run -p 8000:8000 *nome-da-sua-imagem*
3. Abra o navegador e acesse http://localhost:8000

### Credenciais do Admin
login: admin@email.com
senha: admin123 (ou admin12345)

Qualquer fork ou sugestão é bem vinda! 🤗
Contato: lionel.rocha.alves@gmail.com
