from datetime import datetime, timedelta
import random

def random_timestamp_last_week():
    """
    Generate a random timestamp within the last week.
    """
    now = datetime.now()
    one_week_ago = now - timedelta(weeks=1)

    # Generating a random timestamp between now and one week ago
    random_timestamp = one_week_ago + (now - one_week_ago) * random.random()

    # Converting the timestamp to seconds since epoch
    random_timestamp = random_timestamp.timestamp()

    return random_timestamp

# Test the function
print(random_timestamp_last_week())


