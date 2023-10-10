from flask import Flask, stream_with_context, Response
import random
import time
import json

app = Flask(__name__)

@app.route('/generate-stream')
def generate_stream():
    def generate():
        while True:
            # Same mock data generation as before
            user_id = f"user_{random.randint(1, 1000)}"
            events = ['login', 'purchase', 'logout', 'click', 'view']
            event_data = {
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'user_id': user_id,
                'event': random.choice(events),
                'value': random.uniform(0, 100)
            }
            yield f"data: {json.dumps(event_data)}\n\n"  # This structure is required for SSE
            time.sleep(1)  # you can adjust the sleep time to regulate the streaming speed

    return Response(stream_with_context(generate()), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
