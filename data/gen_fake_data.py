import json
import random
import uuid
from datetime import datetime, timedelta

from faker import Faker
from lorem_text import lorem

fake = Faker()
current_date = datetime.now()

values = []

for _ in range(200):
    base_payload = {
        "event_id": uuid.uuid4().__str__(),
        "timestamp": (current_date + timedelta(minutes=1)).strftime('%Y-%m-%dT%H:%M:%S'),
        "domain": "account",
        "event_type": "status-change",
        "data": {
            "id": random.randint(10000, 99999),
            "old_status": "SUSPENDED",
            "new_status": "ACTIVE",
            "reason": lorem.words(random.randint(3, 15))
        }
    }
    values.append(json.dumps(base_payload))

for row in values:
    print(row)