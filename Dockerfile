FROM python:3.10-alpine AS builder

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip && \
    python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt

COPY . .


FROM python:3.10-alpine AS final

RUN apk add --no-cache libmagic

WORKDIR /app

COPY --from=builder /py /py
COPY --from=builder /app /app

RUN addgroup -S user && adduser -S user -G user --no-create-home

RUN chmod -R 755 /app

USER user

EXPOSE 5000

CMD ["/py/bin/flask", "run", "--host", "0.0.0.0"]
