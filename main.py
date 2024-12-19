import click
from .helpers import add_task, list_tasks, mark_task_completed, delete_task

@click.group()
def cli():
    """Task Manager CLI."""
    pass

@click.command()
@click.argument('name')
@click.option('--due', default=None, help='Set a due date for the task.')
@click.option('--priority', default=None, help='Set a priority for the task (e.g., low, medium, high).')
@click.option('--category', default=None, help='Category ID for the task.')
@click.option('--tags', default='', help='Comma separated list of tag IDs for the task.')
def add(name, due, priority, category, tags):
    """Add a new task."""
    tag_ids = list(map(int, tags.split(','))) if tags else []
    add_task(name, due, priority, category, tag_ids)

@click.command()
@click.option('--status', default=None, help='Filter tasks by status.')
@click.option('--priority', default=None, help='Filter tasks by priority.')
def list(status, priority):
    """List all tasks."""
    list_tasks(status, priority)

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

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == '__main__':
    cli()
