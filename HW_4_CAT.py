def get_cats_info(path):
    cat_dict = []  # список для зберігання інформації
    try:
        with open(path, 'r', encoding='utf-8') as file: # відкриваєм фаіл для читання
            for line in file:
                try:
                    id, name, age = line.strip().split(',') # розділяємо дані
                    cat_dict.append({'id': id, 'name': name, 'age': age }) # додаємо інформацію до списку
                except ValueError:
                    print(f"Невірно ведені дані: {line.strip()}")
    except FileNotFoundError:
        # вийняток, коли фаіл не знайдено
        print(f"Фаіл в дерікторії {path}, не знайдено.")
        return None
    return cat_dict

path = 'cats_file.txt'
cat_info = get_cats_info(path)

if cat_info:  # перевіряє, чи список не порожній
    print(cat_info)


