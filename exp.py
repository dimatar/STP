import requests
from db_helper import store_in_postgres
from loguru import logger

URL = "http://127.0.0.1:5000/generate-stream"

def fetch_sse():
    # logger.info("Fetching SSE data from API...")
    # while True:
    with requests.get(URL, stream=True) as response:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith("data: "):
                    data = decoded_line.replace("data: ", "")
                    store_in_postgres(data)
                    logger.info(f"Stored data: {data}")

fetch_sse()