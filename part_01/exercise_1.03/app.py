import time
import uuid
from datetime import datetime

# Generate a random UUID string
unique_id = str(uuid.uuid4())

def log_output():
    while True:
        timestamp = datetime.utcnow().isoformat() + "Z"
        print(f"{timestamp}: {unique_id}")
        time.sleep(5)

if __name__ == "__main__":
    log_output()
