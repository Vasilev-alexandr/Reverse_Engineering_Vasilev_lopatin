import re
import os

# Получаем директорию, где находится сам .py файл
script_dir = os.path.dirname(os.path.abspath(__file__))

# Пути к входному и выходному файлам
input_file = os.path.join(script_dir, "dev.txt")
output_file = os.path.join(script_dir, "result.txt")

# Регулярное выражение для email, оканчивающихся на .site
pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.site\b'

# Чтение файла dev.txt
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Поиск совпадений
emails = re.findall(pattern, text)

# Запись результатов в result.txt
with open(output_file, "w", encoding="utf-8") as file:
    file.write(f"Всего найдено email-адресов с доменом .site: {len(emails)}\n\n")
    for i, email in enumerate(emails, start=1):
        file.write(f"{i}. {email}\n")

# Вывод в консоль
print(f"Всего найдено email-адресов с доменом .site: {len(emails)}\n")
for i, email in enumerate(emails, start=1):
    print(f"{i}. {email}")

print(f"\nРезультаты сохранены в файл: {output_file}")