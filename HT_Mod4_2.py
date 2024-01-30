from pathlib import Path
import re

def get_cats_info(path):
    with open(path, 'r', encoding="utf-8") as files:
        Dic_keys = ["id", "name", "age"]
        fh =str(files.read()) # перетворюємо текст в рядок
        print(type(fh))
        try:  # перевіряємо
            p1 = r"[\w\+\n]+" 
            fh1 = ','.join(re.findall(p1,fh)) 
            print(f" fh1 = {fh1}")
            fh2 = fh1.split() # розділяємо рядок на елементи
            print(f" fh2 = {fh2}") 
            print(len(fh2))

            for i in fh2:
                # print(f"{i}")
                # print(type(i))
                fh3 = i.split() # розділяємо рядок на елементи
                # print(f" fh3 = {fh3}")

                for ii in fh3:
                    fh4 = ii.split(',') # розділяємо рядок на елементи
                    # print(f" fh4 = {fh4}")
                    Numbers = dict(zip(Dic_keys, fh4))
                    print(f"{Numbers}")

        except Exception as error:  # якщ
            print(f"Зчитування файлу неможливе: {error}")

path = Path("Cats_text.txt")
try: # перевіряємо на наявність файлу
    get_cats_info(path)
except Exception as error: 
    print(f"Файл з таким ім'ям відсутній: {error}")