### Install requirements
```
pip install -r requirements.txt
```

### up docker
```
docker-compose up -d
```
### create topic in kafka
```commandline
sudo docker exec -it laba-kafka-1 kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic tasks
```
### run flask app to generate data
```
python app.py
```
### run exp.py to cath data from endpoint and save to postgresql
```
python exp.py
```

