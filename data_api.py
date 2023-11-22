from flask import Flask, stream_with_context, Response
import random
import time
import json
from datetime import datetime, timedelta
from log_config import logger

app = Flask(__name__)

alphabet = "abcdefghijklmnopqrstuvwxyz"


def generate_random_link(domain):
    second_part = ""
    n = 0
    while n <= 6:
        second_part += random.choice(alphabet)
        n += 1

    link = f"https://{domain}/{second_part}/{random.randint(1, 1000)}"
    return link

def random_timestamp_last_week():
    """
    Generate a random timestamp within the last week.
    """
    now = datetime.now()
    one_week_ago = now - timedelta(weeks=24)

    random_timestamp = one_week_ago + (now - one_week_ago) * random.random()

    random_timestamp = random_timestamp.timestamp()

    return random_timestamp

def generate_war_event_data():
    current_timestamp = random_timestamp_last_week()

    lat = round(random.uniform(45.0, 50.0), 5)
    lng = round(random.uniform(31.0, 40.0), 5)

    event_descriptions = {
        "Вибух": "yellow",
        "Спроба прориву": "red",
        "Диверсія у тилу ворога": "green",
        "Диверсія ворога на підконтрольній території": "red",
        "Ураження ворожим дроном": "yellow",
        "Ураження ворожого складу": "green",
        "Підрив автомобіля окупанта": "green",
        "Активність ворожого дрона Shahed-136": "yellow",
        "Активність ворожих дронів Ланцет": "yellow",
    }

    sources = [
        "vk.com",
        "facebook.com",
        "twitter.com",
        "gov.ru",
        "gov.ua"
    ]

    event_description = random.choice(list(event_descriptions.keys()))
    source = random.choice(sources)
    level = event_descriptions[event_description]
    link = generate_random_link(source)

    return {
        "timestamp": current_timestamp,
        "location": {
            "lat": lat,
            "lon": lng,
        },
        "event_description": event_description,
        "source": source,
        "level": level,
        "link": link
    }


@app.route('/generate-stream')
def generate_stream():
    def generate():
        logger.info("Starting to generate mock data")
        while True:
            user_id = f"user_{random.randint(1, 1000)}"
            events = ['login', 'purchase', 'logout', 'click', 'view']
            event_data = generate_war_event_data()
            yield f"{json.dumps(event_data, ensure_ascii=False)}\n\n"
            time.sleep(1)

    return Response(stream_with_context(generate()), content_type='application/json; charset=utf-8')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
