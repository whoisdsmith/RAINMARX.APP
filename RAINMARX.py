import subprocess
import time
import pyfiglet

# Function to display ASCII art title


def print_intro():
    title = pyfiglet.figlet_format("RAINMARX", font="slant")
    print(title)
    print("Welcome to RAINMARX CLI App!")
    print("Your ultimate tool for managing Raindrop.io bookmarks")
    print("=" * 60)

# Function to handle the main menu


def main_menu():
    while True:
        print("\nChoose an option:")
        print("1. Get all bookmarks and nested collections.")
        print("2. Get parent collection by ID.")
        print("3. Update bookmarks from a collection.")
        print("4. Search")
        print("5. Get user stats")
        print("6. Get user collection groups")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            subprocess.run(["python3", "nested.py"])
        elif choice == '2':
            subprocess.run(["python3", "collectid.py"])
        elif choice == '3':
            subprocess.run(["python3", "updatr.py"])
        elif choice == '4':
            subprocess.run(["python3", "search.py"])
        elif choice == '5':
            subprocess.run(["python3", "stats.py"])
        elif choice == '6':
            subprocess.run(["python3", "overview.py"])
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    print_intro()
    time.sleep(2)
    main_menu()


if __name__ == "__main__":
    main()
