import json
import os
import sys
import time
import pika

RABBITMQ_HOST = "localhost"
QUEUE_NAME = "call_tasks"
TASK_DURATION_SECONDS = 30


def run_consumer(consumer_id: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, heartbeat=600)
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    channel.basic_qos(prefetch_count=1)

    def callback(ch, method, properties, body):
        task = json.loads(body.decode("utf-8"))
        t_id = task["id"]
        t_name = task["task_name"]

        task["status"] = "in_progress"
        print(f"[{consumer_id}] POBRANO zadanie: {t_id} ('{t_name}'). Status -> {task['status']}")
        print(f"[{consumer_id}] Wykonywanie pracy ({TASK_DURATION_SECONDS}s)...")

        time.sleep(TASK_DURATION_SECONDS)

        task["status"] = "done"
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"[{consumer_id}] UKOŃCZONO zadanie: {t_id}. Status -> {task['status']}\n")

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    print(f"[{consumer_id}] Połączono z RabbitMQ. Oczekiwanie na zadania (CTRL+C aby zakończyć)...")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print(f"\n[{consumer_id}] Zatrzymywanie consumera...")
        channel.stop_consuming()
    finally:
        connection.close()


if __name__ == "__main__":
    consumer_name = sys.argv[1] if len(sys.argv) > 1 else f"Consumer-{os.getpid()}"
    run_consumer(consumer_name)