import requests
import json
from confluent_kafka import Producer
from loguru import logger
from kafka import KafkaProducer

logger.info("Kafka Producer is starting")
# Налаштування Kafka Producer
# kafka_producer = Producer({'bootstrap.servers': '192.168.50.130:9092'})
producer = KafkaProducer(bootstrap_servers='192.168.50.130:9092')


# Функція для зворотного виклику після відправки
def delivery_report(err, msg):
    logger.info("Delivery report")
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


# Слухаємо Flask ендпоінт
def listen_to_flask_endpoint():
    topic = "tasks"
    logger.info("Listening to Flask endpoint")
    flask_endpoint = "http://localhost:5000/generate-stream"
    with requests.get(flask_endpoint, stream=True) as response:
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode('utf-8'))
                    producer.send(topic, json.dumps(data).encode('utf-8'))
                    producer.flush()
                    logger.info(f"Data sent to Kafka topic: {topic}, data: {data}")
                except Exception as e:
                    logger.error(f"Error sending data to Kafka: {e}")

if __name__ == '__main__':
    listen_to_flask_endpoint()