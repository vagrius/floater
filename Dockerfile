FROM python:3.10-alpine

RUN apk add libffi-dev
RUN apk add gcc musl-dev

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY floater floater
COPY logger.conf logger.conf
COPY run.py run.py

EXPOSE 4099:4099

CMD ["python3", "run.py"]