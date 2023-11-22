# Real-Time Data Streaming and Visualization

This project demonstrates a real-time data streaming and visualization pipeline using Flask, Kafka, ElasticSearch, and Kibana. It generates mock "war event" data, streams it through Kafka, stores it in ElasticSearch, and visualizes it in Kibana.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.10 or later

### Installation

1. **Clone the Repository**:
```commandline
git clone https://github.com/dimatar/STP.git
cd STP/
```

2. **Install Python Dependencies**:
```commandline
pip install -r requirements.txt
```

3. **Start Docker Compose**:
- This will set up Kafka, Zookeeper, ElasticSearch, and Kibana.
  ```
  docker-compose up -d
  ```
  
4. **Create a Kafka Topic**:
- This will create a Kafka topic called `tasks`.
  ```commandline
  docker exec -it kafka kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic tasks
  ```

5. **Run the Flask Application**:
- Starts the data generation process.
  ```
  python data_api.py
  ```

6. **Start Kafka Producer**:
- Sends data from Flask to Kafka.
  ```
  python kafka_producer.py
  ```

7. **Start Kafka Consumer**:
- Consumes data from Kafka and stores it in ElasticSearch.
  ```
  python kafka_consumer.py
  ```

### Logging
- By default, the logs are stored in `./logs.ndjon`.

### Viewing Results in Kibana

1. **Access Kibana Dashboard**:
- Open a browser and navigate to `http://localhost:5601`.

2. **Configure Index Pattern**:
- In Kibana, go to the 'Management' section.
- Under 'Index Patterns', create a new index pattern.
- Use `war_event_v1` as the index pattern name and select `timestamp` as the time filter field.

3. **Create Visualizations**:
- Navigate to the 'Visualize' tab in Kibana.
- Create maps, charts, and graphs based on your data.

4. **Build Dashboard**:
- Combine different visualizations into a dashboard for real-time data monitoring.

5. **Map Visualization**:
- Data can be visualized on a map using the `geoip.location` field.

## Notes

- Ensure all required ports for Kafka, Zookeeper, ElasticSearch, and Kibana are available.
- The configurations can be modified according to your environment.

### Useful Commands

- **List All Kafka Topics**:

```commandline
sudo docker exec -it laba-kafka-1 kafka-topics.sh --list --bootstrap-server localhost:9092
```
- **Delete an Elasticsearch Index**:
```commandline
curl -X DELETE "localhost:9200/war_event_v1"
```
