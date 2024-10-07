
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
# CMD reflex run --env prod --backend-only
FROM python:3.11


WORKDIR /app
COPY . .


ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


RUN reflex init
CMD reflex run --env prod --backend-only