import json
import csv
import re

FILE_NAME = "contacts.json"

# Load contacts
try:
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = []
except Exception as e:
    print("Error loading contacts:", e)
    contacts = []


def save_contacts():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file, indent=4)
    except Exception as e:
        print("Error saving contacts:", e)


def validate_phone(phone):
    return re.match(r"^[0-9]{10}$", phone)


def add_contact():
    try:
        name = input("Enter Name: ")

        while True:
            phone = input("Enter Phone (10 digits): ")
            if validate_phone(phone):
                break
            print("Invalid phone number!")

        email = input("Enter Email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        save_contacts()
        print("Contact added successfully!")

    except Exception as e:
        print("Error:", e)


def search_contact():
    try:
        query = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if query.lower() in contact["name"].lower():
                print("\nName :", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("-" * 30)
                found = True

        if not found:
            print("No matching contacts found.")

    except Exception as e:
        print("Error:", e)


def edit_contact():
    try:
        name = input("Enter contact name to edit: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():

                new_name = input("New Name: ")

                while True:
                    new_phone = input("New Phone (10 digits): ")
                    if validate_phone(new_phone):
                        break
                    print("Invalid phone number!")

                new_email = input("New Email: ")

                contact["name"] = new_name
                contact["phone"] = new_phone
                contact["email"] = new_email

                save_contacts()
                print("Contact updated successfully!")
                return

        print("Contact not found.")

    except Exception as e:
        print("Error:", e)


def delete_contact():
    try:
        name = input("Enter contact name to delete: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                save_contacts()
                print("Contact deleted successfully!")
                return

        print("Contact not found.")

    except Exception as e:
        print("Error:", e)


def list_contacts():
    try:
        if not contacts:
            print("No contacts available.")
            return

        sorted_contacts = sorted(
            contacts,
            key=lambda contact: contact["name"].lower()
        )

        print("\n===== CONTACT LIST =====")

        for contact in sorted_contacts:
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-" * 30)

    except Exception as e:
        print("Error:", e)


def export_csv():
    try:
        with open("contacts.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "phone", "email"]
            )

            writer.writeheader()
            writer.writerows(contacts)

        print("Contacts exported to contacts.csv")

    except Exception as e:
        print("Error exporting CSV:", e)


while True:
    print("\n===== PHONE BOOK MENU =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List Contacts")
    print("6. Export to CSV")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        edit_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        list_contacts()

    elif choice == "6":
        export_csv()

    elif choice == "7":
        save_contacts()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
