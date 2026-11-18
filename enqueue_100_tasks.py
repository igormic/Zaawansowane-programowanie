import subprocess
import sys

TOTAL_TASKS = 100

print(f"Wysyłanie {TOTAL_TASKS} zadań do RabbitMQ przez producer.py...")
for i in range(1, TOTAL_TASKS + 1):
    subprocess.run(
        [sys.executable, "producer.py", f"Rozmowa #{i:03d}"],
        check=True
    )

print(f"\nPomyślnie dodano {TOTAL_TASKS} zadań do kolejki RabbitMQ.")