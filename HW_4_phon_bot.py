def main():
    contacts = {} # словник для зберігання котактів

    def parse_input(user_input):
        # розділяємо введений рядок на команду та аргументи
        parts = user_input.strip().lower().split()
        command = parts[0] # перше слово команда
        args = parts[1:] # решта аргументи
        return command, args

    # функція для додавання контакту
    def add_contact(name, phone):
        if name in contacts:
            return f"Contact {name} already exists."
        contacts[name] = phone
        return "Contact added."

    # функція для зміни номера контакту
    def change_contact(name, phone):
        if name not in contacts:
            return f"Contact {name} not found."
        contacts[name] = phone
        return "Contact updated."

    # функція поверненя номера вказаного контакту
    def show_phone(name):
        if name not in contacts:
            return f"Contact {name} not found."
        return contacts[name]

    # функція повернення всіх збережених номерів
    def show_all():
        if not contacts:
            return "No contacts available."
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

    print("Welcome to the Assistant Bot!")

    while True:
        user_input = input("Enter command: ") # зчитуємо команду
        command, args = parse_input(user_input) # парсім ведення на команду та аргумент

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                print(add_contact(args[0], args[1]))
            else:
                print("Invalid format. Use: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                print(change_contact(args[0], args[1]))
            else:
                print("Invalid format. Use: change [name] [new phone]")
        elif command == "phone":
            if len(args) == 1:
                print(show_phone(args[0]))
            else:
                print("Invalid format. Use: phone [name]")
        elif command == "all":
            print(show_all())
        elif command in ("exit", "close"):
            print("Good bye!")
            break
        else:
            print("Invalid command.")

# виконуємо функцію main(), якшо файл запускається як основний модуль
if __name__ == "__main__":
    main()