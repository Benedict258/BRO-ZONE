def encode(text, key):
    CHARSET_SIZE = 95  # Printable ASCII characters (32 to 126)
    encoded_text = ""
    for char in text:
        if 32 <= ord(char) <= 126:  # Check if character is printable ASCII
            encoded_text += chr(32 + (ord(char) - 32 + key) % CHARSET_SIZE)
        else:
            encoded_text += char  # Preserve non-printable characters
    return encoded_text

def decode(text, key):
    CHARSET_SIZE = 95
    decoded_text = ""
    for char in text:
        if 32 <= ord(char) <= 126:
            decoded_text += chr(32 + (ord(char) - 32 - key) % CHARSET_SIZE)
        else:
            decoded_text += char
    return decoded_text

def bro_menu():
    print("\nWelcome to the Bro Zone!")
    while True:
        print("\nWhat do you want to do?")
        print("1. View Bro Code Rules")
        print("2. Encode/Decode Text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            print("\nBro Code Rules:")
            print("1. Bros before anything else.")
            print("2. Never leave a Bro hanging.")
            print("3. A Bro must always have a Bro's back.")
        elif choice == "2":
            text = input("Enter the text to Encode/Decode: ")
            action = input("Do you want to (1) Encode or (2) Decode? ").strip()
            while True:
                try:
                    key = int(input("Enter a key (0-94): "))
                    if 0 <= key < 95:
                        break
                    print("Invalid key! Please choose a key between 0 and 94.")
                except ValueError:
                    print("Please enter a valid number.")

            if action == "1":
                print("Encoded Text:", encode(text, key))
            elif action == "2":
                print("Decoded Text:", decode(text, key))
            else:
                print("Invalid option. Please try again.")
        elif choice == "3":
            print("PEACE OUT BRO!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    gender = input("ARE YOU A BRO (Y/N)? ").strip().lower()
    if gender == 'y':
        password = input("Enter the Bro Code password: ").strip()
        if password == "A BRO IS NO BRO WITHOUT A BRO":
            bro_menu()
        else:
            print("Wrong password! Access denied.")
    else:
        print("Sorry, this zone is only for Bros!")

if __name__ == "__main__":
    main()
