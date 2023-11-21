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
            "timestamp": {
                "type": "date",
                "format": "epoch_second"
            },
            "location": {
                "type": "geo_point"
            },
            "event_description": {
                "type": "keyword"
            },
            "source": {
                "type": "keyword"
            },
            "level": {
                "type": "keyword"
            },
            "link": {
                "type": "keyword"
            }
        }
    }
}

es = Elasticsearch([es_conf])


def ensure_index():
    logger.info(f"Ensuring index {es_index} exists")
    try:
        if not es.indices.exists(index=es_index):
            es.indices.create(index=es_index, body=es_mapping)
            logger.info(f"Created index {es_index}")
    except es_exceptions.ElasticsearchException as e:
        logger.critical(f"Error creating index: {e}")


def process(data):
    logger.info(f"Processing data: {data}")
    ensure_index()
    es.index(index=es_index, body=data)
    logger.info(f"Message processed and indexed: {data}")
