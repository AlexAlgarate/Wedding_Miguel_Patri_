# ESTE FUNCIONA

# FROM python:3.11


# WORKDIR /app
# COPY . .


# ENV VIRTUAL_ENV=/app/.venv_docker
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# RUN python3.11 -m venv $VIRTUAL_ENV

# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt


# RUN reflex init
# CMD reflex run --env prod --backend-only

# # # # # # # # # 


# Etapa 1: Construcción de la app con Reflex y Python
FROM python:3.12 AS builder

WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt

# Exportar solo el frontend
ENV API_URL="https://weddingmiguelpatri.up.railway.app"
RUN reflex export --frontend-only --no-zip

# Etapa 2: Configurar Nginx para servir el frontend y redirigir al backend
FROM nginx

# Copiar los archivos estáticos del frontend al directorio de Nginx
COPY --from=builder /app/.web/_static /usr/share/nginx/html

# Copiar la configuración personalizada de Nginx
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# # Servir el frontend con Caddy
# FROM caddy:alpine

# # Copiar archivos estáticos exportados por Reflex al contenedor de Caddy
# COPY --from=builder /app/.web/_static /srv

# # Añadir archivo de configuración de Caddy
# COPY Caddyfile /etc/caddy/Caddyfile


# This Dockerfile is used to deploy a simple single-container Reflex app instance.
# FROM python:3.11

# RUN apt-get update && apt-get install -y redis-server && rm -rf /var/lib/apt/lists/*
# ENV REDIS_URL=redis://localhost PYTHONUNBUFFERED=1

# # Copy local context to `/app` inside container (see .dockerignore)
# WORKDIR /app
# COPY . .
# # Copy Caddyfile to the appropriate location
# COPY Caddyfile /etc/caddy/Caddyfile
# # Install app requirements and reflex in the container
# RUN pip install -r requirements.txt

# # Deploy templates and prepare app
# RUN reflex init

# # Download all npm dependencies and compile frontend
# RUN reflex export --frontend-only --no-zip

# # Needed until Reflex properly passes SIGTERM on backend.
# STOPSIGNAL SIGKILL

# # Always apply migrations before starting the backend.
# CMD [ -d alembic ] && reflex db migrate; \
#     redis-server --daemonize yes && \
#     exec reflex run --env prod --backend-only
