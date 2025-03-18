import re
import json
from datetime import datetime

USERS_FILE = "users.json"
PROJECTS_FILE = "projects.json"

def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def validate_egyptian_phone(number):
    pattern = r"^01[0125][0-9]{8}$"
    return re.match(pattern, number) is not None

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def register():
    print("\n--- Registration ---")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    while not validate_email(email):
        print("Invalid email format. Please try again.")
        email = input("Email: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    while password != confirm_password:
        print("Passwords do not match. Please try again.")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")
    mobile = input("Mobile Phone: ")
    while not validate_egyptian_phone(mobile):
        print("Invalid Egyptian phone number. Please try again.")
        mobile = input("Mobile Phone: ")

    users = load_data(USERS_FILE)
    if any(user["email"] == email for user in users):
        print("User already exists.")
        return

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "mobile": mobile,
        "activated": True
    }
    users.append(user)
    save_data(USERS_FILE, users)
    print("Registration successful. You can now login.")

def login():
    print("\n--- Login ---")
    email = input("Email: ")
    password = input("Password: ")

    users = load_data(USERS_FILE)
    for user in users:
        if user["email"] == email and user["password"] == password:
            if user.get("activated", False):
                print("Login successful.")
                return user
            else:
                print("Account not activated. Please activate your account.")
                return None
    print("Invalid email or password.")
    return None

def create_project(user):
    print("\n--- Create Project ---")
    title = input("Title: ")
    details = input("Details: ")
    total_target = float(input("Total Target (EGP): "))
    start_date = input("Start Date (YYYY-MM-DD): ")
    while not validate_date(start_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    while not validate_date(end_date) or end_date <= start_date:
        print("Invalid end date. It must be after the start date.")
        end_date = input("End Date (YYYY-MM-DD): ")

    projects = load_data(PROJECTS_FILE)
    project = {
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_date": start_date,
        "end_date": end_date,
        "user_email": user["email"]
    }
    projects.append(project)
    save_data(PROJECTS_FILE, projects)
    print("Project created successfully.")

def view_projects():
    projects = load_data(PROJECTS_FILE)
    if not projects:
        print("No projects found.")
        return

    print("\n--- All Projects ---")
    for idx, project in enumerate(projects, 1):
        print(f"{idx}. Title: {project['title']}")
        print(f"   Details: {project['details']}")
        print(f"   Target: {project['total_target']} EGP")
        print(f"   Start Date: {project['start_date']}")
        print(f"   End Date: {project['end_date']}")
        print(f"   Created By: {project['user_email']}")
        print()

def edit_project(user):
    projects = load_data(PROJECTS_FILE)
    user_projects = [p for p in projects if p["user_email"] == user["email"]]
    if not user_projects:
        print("You have no projects to edit.")
        return

    print("\n--- Your Projects ---")
    for idx, project in enumerate(user_projects, 1):
        print(f"{idx}. {project['title']}")

    choice = int(input("Select project to edit: ")) - 1
    if 0 <= choice < len(user_projects):
        project = user_projects[choice]
        print(f"Editing: {project['title']}")
        project["title"] = input("New Title: ")
        project["details"] = input("New Details: ")
        project["total_target"] = float(input("New Total Target (EGP): "))
        start_date = input("New Start Date (YYYY-MM-DD): ")
        while not validate_date(start_date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            start_date = input("New Start Date (YYYY-MM-DD): ")
        project["start_date"] = start_date
        end_date = input("New End Date (YYYY-MM-DD): ")
        while not validate_date(end_date) or end_date <= start_date:
            print("Invalid end date. It must be after the start date.")
            end_date = input("New End Date (YYYY-MM-DD): ")
        project["end_date"] = end_date

        save_data(PROJECTS_FILE, projects)
        print("Project updated successfully.")
    else:
        print("Invalid selection.")

def delete_project(user):
    projects = load_data(PROJECTS_FILE)
    user_projects = [p for p in projects if p["user_email"] == user["email"]]
    if not user_projects:
        print("You have no projects to delete.")
        return

    print("\n--- Your Projects ---")
    for idx, project in enumerate(user_projects, 1):
        print(f"{idx}. {project['title']}")

    choice = int(input("Select project to delete: ")) - 1
    if 0 <= choice < len(user_projects):
        project = user_projects[choice]
        projects.remove(project)
        save_data(PROJECTS_FILE, projects)
        print("Project deleted successfully.")
    else:
        print("Invalid selection.")

def main():
    while True:
        print("\n--- Fundraise App ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n--- Main Menu ---")
                    print("1. Create Project")
                    print("2. View All Projects")
                    print("3. Edit Project")
                    print("4. Delete Project")
                    print("5. Logout")
                    sub_choice = input("Choose an option: ")

                    if sub_choice == "1":
                        create_project(user)
                    elif sub_choice == "2":
                        view_projects()
                    elif sub_choice == "3":
                        edit_project(user)
                    elif sub_choice == "4":
                        delete_project(user)
                    elif sub_choice == "5":
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
