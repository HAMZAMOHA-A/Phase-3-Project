# lib/helpers.py
from models import session, Task

def add_task(name):
    """Add a new task to the database."""
    new_task = Task(name=name)
    session.add(new_task)
    session.commit()  # Commit the transaction to the database
    print(f"Task '{name}' added!")

def list_tasks():
    """List all tasks."""
    tasks = session.query(Task).all()
    if tasks:
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task.id}. {task.name} - {status}")
    else:
        print("No tasks found!")

def mark_task_completed(task_id):
    """Mark a task as completed."""
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = True
        session.commit()  # Commit the change
        print(f"Task '{task.name}' marked as completed!")
    else:
        print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    """Delete a task."""
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()  # Commit the delete action
        print(f"Task '{task.name}' deleted!")
    else:
        print(f"Task with ID {task_id} not found.")

def find_task_by_id(task_id):
    """Find a task by its ID."""
    task = session.query(Task).filter(Task.id == task_id).first()  # Query task by ID
    if task:
        status = "Completed" if task.completed else "Pending"
        print(f"Found task: {task.id}. {task.name} - {status}")
    else:
        print(f"Task with ID {task_id} not found.")
