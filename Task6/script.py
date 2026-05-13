import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "dev.txt")

pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.site\b'

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

emails = re.findall(pattern, text)

symbols = {
    '.': [],
    '_': [],
    '%': [],
    '+': [],
    '-': []
}

for email in emails:
    username = email.split("@")[0]
    for s in symbols:
        if s in username:
            symbols[s].append(email)

print("Всего найдено email:", len(emails))
print()

for s, lst in symbols.items():
    print(f"Символ '{s}' используется в {len(lst)} адресах")
    if lst:
        print("Примеры:")
        for e in lst[:3]:
            print(" ", e)
    print()