# Imagen base de Python
FROM python:3.13-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el requirements.txt y el código
COPY requirements.txt .
COPY app/ ./app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Comando para iniciar la app
CMD ["python", "app/vuelos.py"]