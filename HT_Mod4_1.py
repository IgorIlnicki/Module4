from pathlib import Path
import re

def total_salary(path):
    total = 0
    with open(path, 'r', encoding="utf-8") as files:
        fh =str(files.read()) # перетворюємо текст в рядок
        # print(type(fh))
        try:  # перевіряємо 
            p1 = r"\d+" 
            fh1 = ' '.join(re.findall(p1,fh)) 
            # print(f" fh1 = {fh1}")
            fh2 = fh1.split() # розділяємо рядок на елементи
            # print(f" fh2 = {fh2}")
            # print(len(fh2))
            for element in fh2:
                element = int(element)
                # print(f" element = {element}")
                total = total + element 
            average = total/len(fh2)
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

        except Exception as error:  # якщ
            print(f"Зчитування файлу неможливе: {error}")

path = Path("salary_file.txt")
try: # перевіряємо на наявність файлу
    total_salary(path)
except Exception as error: 
    print(f"Файл з таким ім'ям відсутній: {error}")


