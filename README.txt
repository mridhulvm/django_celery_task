
The important aspect of this project is background tasks run by celery
supported by default broker RabbitMQ.

installation and configuration of RabbitMQ server.

    $sudo apt-get install rabbitmq-server

    $sudo systemctl enable rabbitmq-server

    $sudo systemctl start rabbitmq-server

    $systemctl status rabbitmq-server

So run celery worker in the background along with django server as below.

    $celery -A QueueProject worker -l info


