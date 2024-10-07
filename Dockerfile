
FROM python:3.12 AS builder

ARG PATRI_PHONE
ARG MIGUEL_PHONE
ARG ACCOUNT_NUMBER
ARG SUPABASE_KEY
ARG SUPABASE_URL
WORKDIR /app

COPY . .
ENV PATRI_PHONE=${PATRI_PHONE}
ENV MIGUEL_PHONE=${MIGUEL_PHONE}
ENV ACCOUNT_NUMBER=${ACCOUNT_NUMBER}
ENV SUPABASE_KEY=${SUPABASE_KEY}
ENV SUPABASE_URL=${SUPABASE_URL}
RUN pip install -r requirements.txt
RUN API_URL="https://wedding-miguel-patri-backend.vercel.app/"
RUN reflex export --frontend-only --no-zip


FROM nginx


COPY --from=builder /app/.web/_static /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf