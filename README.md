### Install requirements
```
pip install -r requirements.txt
```

### up docker
```
docker-compose up -d
```
### create postgresql database
- create database 'db'
- create schema 'data'
- create table 'temp_data' in schema 'data'
- create columns 'id serial' and 'data text'
### run flask app to generate data
```
python app.py
```
### run exp.py to cath data from endpoint and save to postgresql
```
python exp.py
```

