FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY app/requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código completo
COPY . .

# Crear directorio para la BD
# Crear directorio para la BD
RUN mkdir -p /app/instance

# Exponer puerto
EXPOSE 5000

# Ejecutar app directamente (sin inicialización, ya que la BD está lista)
CMD python -u app/run.py
