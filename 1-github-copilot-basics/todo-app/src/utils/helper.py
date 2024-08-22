# helper.py

def format_date(date):
    """
    Format a date object to a string representation.
    """
    return date.strftime("%Y-%m-%d")

def validate_task(task):
    """
    Validate a task object to ensure it has the required fields.
    """
    if not task.get('title'):
        raise ValueError("Task title is required.")
    if not task.get('due_date'):
        raise ValueError("Task due date is required.")

def generate_task_id():
    """
    Generate a unique task ID.
    """
    # Implementation logic for generating a unique task ID
    pass

# Other utility functions or helper classes can be added here