from celery import Celery

app = Celery('consumer', backend='redis://localhost',
             broker='pyamqp://rabbitmq:rabbitmq@localhost//')


@app.task
def add(x, y):
    return x + y
