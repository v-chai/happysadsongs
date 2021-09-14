FROM python:3.8.6-buster

COPY raw_data/twoclass_roberta_bin /raw_data/twoclass_roberta_bin
COPY happysadsongs /happysadsongs
COPY api /api
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
