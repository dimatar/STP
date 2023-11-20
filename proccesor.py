from confluent_kafka import Consumer, KafkaException
from elasticsearch import Elasticsearch, exceptions as es_exceptions
import json
from loguru import logger

es_conf = {
    'host': 'localhost',
    'port': 9200,
    'scheme': 'http'
}
es_index = "war_event_v1"
es_mapping = {
    "mappings": {
        "properties": {
            "timestamp": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
            "user_id": {"type": "keyword"},
            "event": {"type": "keyword"},
            "value": {"type": "float"}
        }
    }
}


es = Elasticsearch([es_conf])


# Ensure the Elasticsearch index exists
def ensure_index():
    logger.info(f"Ensuring index {es_index} exists")
    try:
        if not es.indices.exists(index=es_index):
            es.indices.create(index=es_index, body=es_mapping)
            print(f"Created index {es_index}")
    except es_exceptions.ElasticsearchException as e:
        print(f"Error creating index: {e}")


# Process function (to be implemented by you)
def process(data):
    logger.info(f"Processing data: {data}")
    ensure_index()
    es.index(index=es_index, body=data)
    print(f"Message processed and indexed: {data}")
