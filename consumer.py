import csv
import fcntl
import os
import sys
import time

QUEUE_FILE = "queue.csv"
FIELDNAMES = ["id", "task_name", "status", "created_at", "updated_at"]
TASK_DURATION_SECONDS = 30
CHECK_INTERVAL_SECONDS = 5


def read_and_lock_tasks(f) -> list[dict]:
    fcntl.flock(f, fcntl.LOCK_EX)
    f.seek(0)
    reader = csv.DictReader(f)
    return list(reader)


def save_tasks_and_unlock(f, tasks: list[dict]) -> None:
    f.seek(0)
    f.truncate()
    writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(tasks)
    f.flush()
    fcntl.flock(f, fcntl.LOCK_UN)


def acquire_pending_task():
    if not os.path.exists(QUEUE_FILE):
        return None

    with open(QUEUE_FILE, "r+", newline="", encoding="utf-8") as f:
        tasks = read_and_lock_tasks(f)
        task_to_run = None

        for task in tasks:
            if task["status"] == "pending":
                task["status"] = "in_progress"
                task["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
                task_to_run = dict(task)
                break

        save_tasks_and_unlock(f, tasks)
        return task_to_run


def mark_task_as_done(task_id: str) -> None:
    if not os.path.exists(QUEUE_FILE):
        return

    with open(QUEUE_FILE, "r+", newline="", encoding="utf-8") as f:
        tasks = read_and_lock_tasks(f)
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
                break
        save_tasks_and_unlock(f, tasks)


def run_consumer(consumer_id: str):
    print(f"[{consumer_id}] Uruchomiono consumera. Oczekiwanie na zadania...")
    while True:
        try:
            task = acquire_pending_task()

            if task:
                t_id = task["id"]
                t_name = task["task_name"]
                print(f"[{consumer_id}] POBRANO zadanie: {t_id} ('{t_name}'). Zmiana statusu -> in_progress")
                print(f"[{consumer_id}] Praca w toku ({TASK_DURATION_SECONDS}s)...")

                time.sleep(TASK_DURATION_SECONDS)

                mark_task_as_done(t_id)
                print(f"[{consumer_id}] UKOŃCZONO zadanie: {t_id}. Zmiana statusu -> done\n")
            else:
                time.sleep(CHECK_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            print(f"\n[{consumer_id}] Zatrzymywanie consumera...")
            break


if __name__ == "__main__":
    consumer_name = sys.argv[1] if len(sys.argv) > 1 else f"Consumer-{os.getpid()}"
    run_consumer(consumer_name)