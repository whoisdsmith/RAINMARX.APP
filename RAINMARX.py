import subprocess


def main():
    while True:
        print("Choose an option:")
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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
