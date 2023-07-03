import time

import pika
from core import RABBIT_CONN_STR, RABBIT_QUEUE
from log import get_logger

from .send_email import send_email


logger = get_logger(__name__)


def queue_handler():
    rabbit_conn_str: str = RABBIT_CONN_STR

    while True:
        try:
            logger.info(f"Try to connect to `{rabbit_conn_str}`...")
            connection = pika.BlockingConnection(
                pika.URLParameters(rabbit_conn_str)
            )
            logger.info("Successfully connected...")
            break
        except pika.exceptions.AMQPConnectionError as e:
            logger.error(e)
            logger.error("Connection error! Try in 5.0s")
            time.sleep(5)

    channel = connection.channel()

    # сохраняемая очередь
    channel.queue_declare(queue=RABBIT_QUEUE, durable=True)

    # не распределять новые задачи этому обработчику пока он не обработает текущую
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=RABBIT_QUEUE, on_message_callback=send_email)

    logger.info(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
