import json
import sys
import time
import uuid
import pika

RABBITMQ_HOST = "localhost"
QUEUE_NAME = "call_tasks"


def add_task(task_name: str) -> str:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    task_id = str(uuid.uuid4())[:8]
    payload = {
        "id": task_id,
        "task_name": task_name,
        "status": "pending",
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=json.dumps(payload, ensure_ascii=False),
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        ),
    )

    print(f"[PRODUCER] Wysłano zadanie: {task_id} - '{task_name}' (status: pending)")
    connection.close()
    return task_id


if __name__ == "__main__":
    task_desc = sys.argv[1] if len(sys.argv) > 1 else "Rozmowa telefoniczna z klientem"
    add_task(task_desc)