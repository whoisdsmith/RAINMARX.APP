import subprocess
import time
import pyfiglet
import threading

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
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            subprocess.run(["python3", "nested.py"])
        elif choice == '2':
            subprocess.run(["python3", "collectid.py"])
        elif choice == '3':
            subprocess.run(["python3", "updatr.py"])
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to run the main menu with a timeout


def main():
    print_intro()
    time.sleep(2)

    # Start the main menu in a separate thread
    menu_thread = threading.Thread(target=main_menu)
    menu_thread.start()

    # Wait for the thread to finish or timeout
    menu_thread.join(timeout=15)

    if menu_thread.is_alive():
        print("\nNo activity detected. Exiting automatically... Goodbye!")
        menu_thread.join()  # Ensure the thread is properly terminated


if __name__ == "__main__":
    main()
