
The important aspect of this project is background tasks run by celery
supported by default broker RabbitMQ.

So run celery worker in the background along with django server as below.

$celery -A QueueProject worker -l info


