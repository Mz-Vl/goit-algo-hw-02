from queue import Queue

queue_request = Queue()

request_number = 0


def generate_request():
    global request_number
    request_number += 1
    request_data = f"Заявка No_{request_number}"
    queue_request.put(request_data)
    print(f"\n<<< Заявка No_{request_number} створена >>>\n")


def process_request():
    if not queue_request.empty():
        processed_request = queue_request.get()
        print(f"\n<<< Заявка {processed_request} оброблена>>>\n")
    else:
        print("\n!!! Черга пуста !!!\n")


if __name__ == "__main__":
    while True:
        print("\n1 - Створити нову заявку")
        print("2 - Обробити заявку")
        print("0 - Вийти з програми\n")
        choice = input("\n______________________________\n| Вітаємо у сервісному центрі \n| Виберіть опцію: ")

        if choice == "1":
            generate_request()
        elif choice == "2":
            process_request()
        elif choice == "0":
            print("--- Програма завершила роботу. ---")
            break
        else:
            print("\n!!! Невірний вибір. Спробуйте ще раз. !!!\n")
