# Import necessary modules and files
from models import Task, User
from views import display_tasks, get_user_input, user_login, user_register
from controllers import add_task, delete_task

# Main function to run the to-do app
def main():
    users = []  # List to store users
    tasks = []  # List to store tasks

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_register()
        elif choice == "2":
            user_login()
            break
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please try again.")

    while True:
        display_tasks(tasks)  # Display tasks to the user
        choice = get_user_input()  # Get user input

        if choice == "1":
            task_name = input("Enter task name: ")
            task = Task(task_name)
            add_task(tasks, task)  # Add task to the list
        elif choice == "2":
            task_index = int(input("Enter task index to delete: "))
            delete_task(tasks, task_index)  # Delete task from the list
        elif choice == "3":
            break  # Exit the app
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()