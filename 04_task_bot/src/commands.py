from src.decorator import input_error

@input_error
def add_contact(args, contacts):
     """Додає контакт у словник."""
     if len(args) != 2:
        return "Invalid input. Usage: add [name] [phone]"
     name, phone = args
     contacts[name] = phone
     return "Contact added."

@input_error
def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    if len(args) != 2:
        return "Invalid input. Usage: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."

@input_error
def show_phone(args, contacts):
    """Повертає номер телефону за іменем."""
    if len(args) != 1:
        return "Invalid input. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]  # Повертаємо лише номер телефону
    return "Contact not found."

@input_error
def show_all(contacts):
    """Показує всі контакти."""
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

