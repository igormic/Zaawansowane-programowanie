import sys
from database import get_db, init_db


def add_task(task_name: str) -> int:
    init_db()
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO tasks (task_name, status, created_at, updated_at)
            VALUES (?, 'pending', datetime('now', 'localtime'), datetime('now', 'localtime'))
            """,
            (task_name,),
        )
        conn.commit()
        task_id = cursor.lastrowid

    print(f"[PRODUCER] Zapisano zadanie ID: {task_id} - '{task_name}' (status: pending)")
    return task_id


if __name__ == "__main__":
    task_desc = sys.argv[1] if len(sys.argv) > 1 else "Rozmowa telefoniczna z klientem"
    add_task(task_desc)