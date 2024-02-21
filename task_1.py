import time
from queue import Queue

# Черга заявок
request_queue = Queue()

# ID заявок
request_id = 1

def generate_request(id):
	# Нова заявка
	new_request = f"заявка #{id}"
	
	# Додаєм заявку до черги
	request_queue.put(new_request)
	print(f"Згенерована {new_request}")
	time.sleep(1)

def process_request():
	# Якщо черга не пуста:
	if not request_queue.empty():

		# Видалити заявку з черги
		request = request_queue.get()

		# Обробити заявку
		print(f"Оброблена {request}")
		time.sleep(1)
	else:
	# Вивести повідомлення, що черга пуста
		print("Черга пуста...")

try:
	while True:
		generate_request(request_id)
		request_id += 1
		process_request()
except KeyboardInterrupt:
	print('Обробка заявок зупинена.')