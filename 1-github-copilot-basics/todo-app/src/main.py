# Import necessary modules and files
from models import Task
from views import display_tasks, get_user_input
from controllers import add_task, delete_task

# Main function to run the to-do app
def main():
    tasks = []  # List to store tasks

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