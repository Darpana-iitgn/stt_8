FROM python:3.9-alpine as builder

WORKDIR /app
COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --user --no-cache-dir -r requirements.txt \
    && apk del .build-deps

FROM python:3.9-alpine

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY main.py .

ENV PATH=/root/.local/bin:$PATH
EXPOSE 9567

RUN python -m compileall -b /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9567"]