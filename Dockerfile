# Use uma imagem base adequada para o seu aplicativo
FROM python:3.8

WORKDIR /app

# Copie os arquivos necessários para o contêiner
COPY . .

# Instale as dependências do seu aplicativo
RUN pip install --no-cache-dir -r requirements.txt

# Especifique o comando a ser executado quando o contêiner for iniciado
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
