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


# Stage 1: init
FROM python:3.11 as init
COPY .env /app/.env

# Cargar variables de entorno desde el archivo .env
ENV $(cat /app/.env | xargs)

ARG uv=/root/.cargo/bin/uv

# Install `uv` for faster package boostrapping
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .
RUN mkdir -p /app/data /app/uploaded_files

# Create virtualenv which will be copied into final container
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN $uv venv

# Install app requirements and reflex inside virtualenv
RUN $uv pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Export static copy of frontend to /app/.web/_static
RUN reflex export --frontend-only --no-zip

# Copy static files out of /app to save space in backend image
RUN mv .web/_static /tmp/_static
RUN rm -rf .web && mkdir .web
RUN mv /tmp/_static .web/_static

# Stage 2: copy artifacts into slim image 
FROM python:3.11-slim
WORKDIR /app
RUN adduser --disabled-password --home /app reflex
COPY --chown=reflex --from=init /app /app


# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

# Always apply migrations before starting the backend.
CMD [ -d alembic ] && reflex db migrate; \
    exec reflex run --env prod --backend-only