from celery import Celery

celery = Celery("notelink", broker="amqp://guest:guest@rabbitmq:5672")

celery.conf.update(
    result_backend="rpc://",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Europe/London",
    enable_utc=True,
)
