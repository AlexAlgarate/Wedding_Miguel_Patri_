
# FROM python:3.12 AS builder

# ARG PATRI_PHONE
# ARG MIGUEL_PHONE
# ARG ACCOUNT_NUMBER
# ARG SUPABASE_KEY
# ARG SUPABASE_URL
# WORKDIR /app

# COPY . .
# ENV PATRI_PHONE=${PATRI_PHONE}
# ENV MIGUEL_PHONE=${MIGUEL_PHONE}
# ENV ACCOUNT_NUMBER=${ACCOUNT_NUMBER}
# ENV SUPABASE_KEY=${SUPABASE_KEY}
# ENV SUPABASE_URL=${SUPABASE_URL}
# RUN pip install -r requirements.txt
# RUN API_URL="https://wedding-miguel-patri-backend.vercel.app/"
# RUN reflex export --frontend-only --no-zip


# FROM nginx


# COPY --from=builder /app/.web/_static /usr/share/nginx/html
# COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# COPY --from=builder /app/.web/_static /usr/share/nginx/html
# CMD reflex run --env prod --backend-only
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

# Stage 1: init
FROM python:3.11 as init
ARG PATRI_PHONE
ARG MIGUEL_PHONE
ARG ACCOUNT_NUMBER
ARG SUPABASE_KEY
ARG SUPABASE_URL
ARG uv=/root/.cargo/bin/uv

# Install `uv` for faster package boostrapping
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .
ENV PATRI_PHONE=${PATRI_PHONE}
ENV MIGUEL_PHONE=${MIGUEL_PHONE}
ENV ACCOUNT_NUMBER=${ACCOUNT_NUMBER}
ENV SUPABASE_KEY=${SUPABASE_KEY}
ENV SUPABASE_URL=${SUPABASE_URL}

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
# Install libpq-dev for psycopg2 (skip if not using postgres).
RUN apt-get update -y && rm -rf /var/lib/apt/lists/*
USER reflex
ENV PATH="/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

# Always apply migrations before starting the backend.
CMD [ -d alembic ] && reflex db migrate; \
    exec reflex run --env prod --backend-only