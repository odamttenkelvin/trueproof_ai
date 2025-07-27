import hashlib
import json
import os
from datetime import datetime

def log_to_blockchain(data):
    hash_value = hashlib.sha256(data.encode()).hexdigest()
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "hash": hash_value
    }
    os.makedirs("outputs/hashes", exist_ok=True)
    log_path = "outputs/hashes/log.json"
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(entry)
    with open(log_path, "w") as f:
        json.dump(logs, f, indent=2)
    return entry