import os
import sys
import time
from database import get_db, init_db

TASK_DURATION_SECONDS = 30
CHECK_INTERVAL_SECONDS = 5


def acquire_pending_task():
    """Atomowo pobiera najstarsze zadanie 'pending' i oznacza je jako 'in_progress'."""
    with get_db() as conn:
        conn.execute("BEGIN IMMEDIATE;")
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, task_name FROM tasks
            WHERE status = 'pending'
            ORDER BY id ASC
            LIMIT 1;
            """
        )
        row = cursor.fetchone()

        if row is None:
            conn.commit()
            return None

        task_id = row["id"]
        cursor.execute(
            """
            UPDATE tasks
            SET status = 'in_progress', updated_at = datetime('now', 'localtime')
            WHERE id = ?;
            """,
            (task_id,),
        )
        conn.commit()
        return dict(row)


def mark_task_as_done(task_id: int) -> None:
    with get_db() as conn:
        conn.execute(
            """
            UPDATE tasks
            SET status = 'done', updated_at = datetime('now', 'localtime')
            WHERE id = ?;
            """,
            (task_id,),
        )
        conn.commit()


def run_consumer(consumer_id: str):
    init_db()
    print(f"[{consumer_id}] Uruchomiono consumera. Oczekiwanie na zadania...")

    while True:
        try:
            task = acquire_pending_task()

            if task:
                t_id = task["id"]
                t_name = task["task_name"]
                print(f"[{consumer_id}] POBRANO zadanie ID {t_id} ('{t_name}'). Status -> in_progress")
                print(f"[{consumer_id}] Wykonywanie pracy ({TASK_DURATION_SECONDS}s)...")

                time.sleep(TASK_DURATION_SECONDS)

                mark_task_as_done(t_id)
                print(f"[{consumer_id}] UKOŃCZONO zadanie ID {t_id}. Status -> done\n")
            else:
                time.sleep(CHECK_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            print(f"\n[{consumer_id}] Zatrzymywanie consumera...")
            break


if __name__ == "__main__":
    consumer_name = sys.argv[1] if len(sys.argv) > 1 else f"Consumer-{os.getpid()}"
    run_consumer(consumer_name)