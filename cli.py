# cli.py
import click
from helpers import add_task, list_tasks, mark_task_completed, delete_task, find_task_by_id

@click.group()
def cli():
    """Task Manager CLI."""
    pass

@click.command()
@click.argument('name')
def add(name):
    """Add a new task."""
    add_task(name)

@click.command()
def list():
    """List all tasks."""
    list_tasks()

@click.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Mark a task as completed."""
    mark_task_completed(task_id)

@click.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task."""
    delete_task(task_id)

@click.command()
@click.argument('task_id', type=int)
def find_task(task_id):
    """Find a task by its ID."""
    find_task_by_id(task_id)

# Add the commands to the CLI group
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)
cli.add_command(find_task)  # Ensure this line is present

if __name__ == '__main__':
    cli()
