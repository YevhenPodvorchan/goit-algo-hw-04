# розділяємо введений рядок на команду та аргументи
def parse_input(user_input):
    parts = user_input.strip().lower().split()
    command = parts[0]  # перше слово команда
    args = parts[1:]  # решта аргументи
    return command, args


# функція для додавання контакту
def add_contact(contacts, *args):
    if len(args) != 2:  # перевірка кількості аргументів
        return("Invalid format. Use: add [name] [phone]")
    name, phone  = args
    if name in contacts:
        return f"Contact {name} already exists."
    contacts[name] = phone
    return "Contact added."


# функція для зміни номера контакту
def change_contact(contacts, *args):
    if len(args) != 2:
        return f"Invalid format. Use: change [name] [new phone]"
    name, phone = args
    if name not in contacts:
            return f"Contact {name} not found."
    contacts[name] = phone
    return "Contact updated."


# функція поверненя номера вказаного контакту
def show_phone(contacts, *args):
    if len(args) != 1:
        return "Invalid format. Use: phone [name]"
    name = args[0]
    if name not in contacts:
        return f"Contact {name} not found."
    return contacts[name]


# функція повернення всіх збережених номерів
def show_all(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


# Основна функція
def main():
    contacts = {} # словник для зберігання котактів

    print("Welcome to the Assistant Bot!")

    while True:
        user_input = input("Enter command: ") # зчитуємо команду
        command, args = parse_input(user_input) # парсім ведення на команду та аргумент

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(contacts,*args))
        elif command == "change":
            print(change_contact(contacts,*args))
        elif command == "phone":
                print(show_phone(contacts,*args))
        elif command == "all":
            print(show_all(contacts))
        elif command in ("exit", "close"):
            print("Good bye!")
            break
        else:
            print("Invalid command.")

# виконуємо функцію main(), якшо файл запускається як основний модуль
if __name__ == "__main__":
    main()
