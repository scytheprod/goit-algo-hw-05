def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Invalid command!"
        except IndexError:
            return "Invalid command!"

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_contact(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."
@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact '{name}' updated."
    else:
        return f"Contact '{name}' not found."

@input_error
def show_all(args, contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye"]:
            print("Good bye!")
            break
        elif command == "phone":
            if args:
                print(show_contact(args[0], contacts))
            else:
                print("Input name after 'phone'.")
        elif command == "all":
            print(show_all(args, contacts))
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args,contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
