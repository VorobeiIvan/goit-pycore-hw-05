from src.decorator import input_error

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide both name and new phone number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Please provide a name."
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    return "Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
