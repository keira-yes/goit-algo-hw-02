from collections import deque

# Приймаємо строку від юзера
input = input("Введіть фразу для перевірки:")

# Робимо строку нечутливою до регістру, знаків та пробілів
str_processed = "".join(letter.lower() for letter in input if letter.isalpha())

# Додаємо строку до двосторонньої черги
str_deque = deque(str_processed)

def checkPalindrom(str):
	# Передбачаємо непарну кількість символів
	while len(str) > 1:
		# Порівнюємо лівий та правий символ черги
		if str.popleft() != str.pop():
			print(f"Фраза '{input}' не є паліндром")
			return False

	print(f"Фраза '{input}' - паліндром")	
	return True

checkPalindrom(str_deque)

