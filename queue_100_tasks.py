import subprocess
import sys

TOTAL_TASKS = 100

print(f"Dodawanie {TOTAL_TASKS} zadań do SQLite przez producer.py...")
for i in range(1, TOTAL_TASKS + 1):
    subprocess.run(
        [sys.executable, "producer.py", f"Rozmowa #{i:03d}"],
        check=True
    )

print(f"\nPomyślnie dodano {TOTAL_TASKS} zadań do bazy.")