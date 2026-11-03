import csv
import fcntl
import os
import sys
import time
import uuid

QUEUE_FILE = "queue.csv"
FIELDNAMES = ["id", "task_name", "status", "created_at", "updated_at"]


def init_queue_file() -> None:
    if not os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_task(task_name: str) -> str:
    init_queue_file()
    task_id = str(uuid.uuid4())[:8]
    now = time.strftime("%Y-%m-%d %H:%M:%S")

    row = {
        "id": task_id,
        "task_name": task_name,
        "status": "pending",
        "created_at": now,
        "updated_at": now,
    }

    with open(QUEUE_FILE, "a+", newline="", encoding="utf-8") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writerow(row)
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)

    print(f"[PRODUCER] Zapisano zadanie: {task_id} - '{task_name}' (status: pending)")
    return task_id


if __name__ == "__main__":
    task_desc = sys.argv[1] if len(sys.argv) > 1 else "Rozmowa telefoniczna z klientem"
    add_task(task_desc)