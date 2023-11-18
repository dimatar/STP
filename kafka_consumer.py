from confluent_kafka import Consumer, KafkaError
from elasticsearch import Elasticsearch
from loguru import logger

from kafka import KafkaConsumer


logger.info("Kafka Consumer is starting")

#
# consumer = KafkaConsumer(
#     'tasks',
#      bootstrap_servers=['10.17.48.245:9092'],
#      auto_offset_reset='latest',
#      enable_auto_commit=True,
#      group_id='test-consumer-group',
#      value_deserializer=lambda x: loads(x.decode('ISO-8859-1')))


# Налаштування Kafka Consumer
conf = {
    'bootstrap.servers': '0.0.0.0:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'latest'
}
consumer = Consumer(conf)


# Підключення до Elasticsearch
# es = Elasticsearch(['http://localhost:9200'])

def process_data(data):
    logger.info(f"Data received from Kafka, data: {data}")


def consume_loop(consumer, topics):
    logger.info("Listening to Kafka topic")
    try:
        consumer.subscribe(topics)

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue
            logger.info(f"Message received from Kafka, message: {msg}")
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            process_data(msg.value().decode('utf-8'))

    finally:
        consumer.close()


if __name__ == '__main__':
    topics = ['tasks']
    consume_loop(consumer, topics)
