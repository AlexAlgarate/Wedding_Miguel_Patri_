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


# This Dockerfile is used to deploy a simple single-container Reflex app instance.
FROM python:3.11

RUN apt-get update && apt-get install -y redis-server && rm -rf /var/lib/apt/lists/*
ENV REDIS_URL=redis://localhost PYTHONUNBUFFERED=1

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .
# Copy Caddyfile to the appropriate location
COPY Caddyfile /etc/caddy/Caddyfile
# Install app requirements and reflex in the container
RUN pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Download all npm dependencies and compile frontend
RUN reflex export --frontend-only --no-zip

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

# Always apply migrations before starting the backend.
CMD [ -d alembic ] && reflex db migrate; \
    redis-server --daemonize yes && \
    exec reflex run --env prod --backend-only
