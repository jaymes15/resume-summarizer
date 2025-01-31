FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

COPY ./scripts/ /scripts/

RUN chmod +x /scripts/*

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./app /app

RUN adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol

RUN chmod -R 777 /vol/web


ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]
