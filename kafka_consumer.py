import time
from json import loads
from kafka import KafkaConsumer
from loguru import logger

from proccesor import process

logger.info("Kafka Consumer is starting")

consumer = KafkaConsumer(
    'tasks',
    bootstrap_servers=['192.168.50.130:9094'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='processor',
    value_deserializer=lambda x: loads(x.decode('ISO-8859-1'))
)


def process_data(data):
    process(data)


def consume_loop(consumer, topics):
    logger.info("Listening to Kafka topic")
    try:
        consumer.subscribe(topics)

        for msg in consumer:
            if msg is None:
                continue
            logger.info(f"Message received from Kafka, message: {msg}")
            process_data(msg.value)


    finally:
        consumer.close()


if __name__ == '__main__':
    topics = ['tasks']
    consume_loop(consumer, topics)
