import random
import time
from queue import Queue

queue_request = Queue()

request_number = 0


def generate_request():
    global request_number
    request_number += 1
    request_data = f"Заявка No_{request_number}"
    queue_request.put(request_data)
    print(f"Заявка No_{request_number} створена")


def process_request():
    if not queue_request.empty():
        processed_request = queue_request.get()
        print(f"Заявка {processed_request} оброблена\n")
    else:
        print("Черга пуста")


while True:
    new_request_created = False

    sleep_interval1 = random.randint(1, 5)
    time.sleep(sleep_interval1)
    generate_request()
    new_request_created = True


    if new_request_created:
        sleep_interval2 = random.randint(1, 5)
        time.sleep(sleep_interval2)
        process_request()

