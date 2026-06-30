import pwinput
def add_password():
    website = input("Enter Website: ")
    username = input("Enter Username: ")
    password = pwinput.pwinput(prompt="Enter password:")

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {username} | {password}\n")

    print("Password saved successfully!\n")


def view_password():
    try:
        with open("passwords.txt", "r") as file:
            data = file.read()

            if data:
                print("\n===== Saved Passwords =====")
                print(data)
            else:
                print("No passwords saved.")

    except FileNotFoundError:
        print("No password file found.")


while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_password()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")