# How to run

## Backend and Broker

```bash
docker compose up
```

## Consumer

```bash
celery -A src.consumer worker --loglevel=INFO
```

## Producer

```bash
python src/producer.py
```
