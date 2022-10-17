import random
from celery import Celery

app = Celery('producer', backend='redis://localhost',
             broker='pyamqp://rabbitmq:rabbitmq@localhost//')

if __name__ == "__main__":
    number_1 = random.randint(1, 10)
    number_2 = random.randint(10, 100)

    print(f"Adding up {number_1} to {number_2}")

    result = app.send_task('src.consumer.add', args=[number_1, number_2])

    print(f"task id: {result}")
    print(f"result: {result.get()}")
