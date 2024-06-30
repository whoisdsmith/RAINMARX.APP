import subprocess
import time
import pyfiglet


def print_intro():
    title = pyfiglet.figlet_format("RAINMARX", font="slant")
    print(title)
    print("Welcome to RAINMARX CLI App!")
    print("Your ultimate tool for managing Raindrop.io bookmarks")
    print("=" * 60)


def main():
    print_intro()
    time.sleep(2)

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


if __name__ == "__main__":
    main()
