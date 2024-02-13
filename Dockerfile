# Use uma imagem base adequada para o seu aplicativo
FROM python:3.8

# Defina o diretório de trabalho dentro do contêiner
WORKDIR .

# Copie os arquivos necessários para o contêiner
COPY . /app
RUN cat requirements.txt

# Instale as dependências do seu aplicativo
RUN pip install --no-cache-dir -r requirements.txt

# Especifique o comando a ser executado quando o contêiner for iniciado
CMD ["python", "manage.py runserver"]
