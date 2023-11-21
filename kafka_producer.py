import requests
import json
from loguru import logger
from kafka import KafkaProducer

logger.info("Kafka Producer is starting")
producer = KafkaProducer(bootstrap_servers='192.168.50.130:9094')


def on_send_success(record_metadata):
    logger.info(
        f"Message sent to {record_metadata.topic} partition {record_metadata.partition} offset {record_metadata.offset}")


def on_send_error(excp):
    logger.error(f'Message delivery failed: {excp}')


# Слухаємо Flask ендпоінт
def listen_to_flask_endpoint():
    topic = "tasks"
    logger.info("Listening to Flask endpoint")
    flask_endpoint = "http://localhost:5000/generate-stream"
    with requests.get(flask_endpoint, stream=True) as response:
        for line in response.iter_lines():
            if line:
                logger.info("Got message from Flask endpoint, trying to send it to Kafka")
                try:
                    data = json.loads(line.decode('utf-8'))
                    producer.send(topic, json.dumps(data).encode('utf-8')).add_callback(on_send_success).add_errback(
                        on_send_error)
                    producer.flush()
                    logger.info(f"Data sent to Kafka topic: {topic}, data: {data}")
                except Exception as e:
                    logger.error(f"Error sending data to Kafka: {e}")


if __name__ == '__main__':
    listen_to_flask_endpoint()
