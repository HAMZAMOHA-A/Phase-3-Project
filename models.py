from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # Unique constraint on category name

    # Relationship: One Category can have many Tasks
    tasks = relationship("Task", back_populates="category", cascade="all, delete-orphan")

    @classmethod
    def create(cls, session, name):
        """Create a new category."""
        if session.query(cls).filter_by(name=name).first():
            raise ValueError(f"Category with name {name} already exists.")
        category = cls(name=name)
        session.add(category)
        session.commit()
        return category

    @classmethod
    def delete(cls, session, category_id):
        """Delete a category by its ID."""
        category = session.query(cls).filter_by(id=category_id).first()
        if category:
            session.delete(category)
            session.commit()
        else:
            raise ValueError(f"Category with ID {category_id} not found.")

    @classmethod
    def get_all(cls, session):
        """Get all categories."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, category_id):
        """Find a category by its ID."""
        return session.query(cls).filter_by(id=category_id).first()

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Task name cannot be null
    completed = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey('categories.id'))  # ForeignKey to 'categories' table

    # Relationship: One Task belongs to one Category
    category = relationship("Category", back_populates="tasks")

    @property
    def is_completed(self):
        """Property method to check if task is completed."""
        return self.completed

    @is_completed.setter
    def is_completed(self, value):
        """Property method to set task completion status."""
        if not isinstance(value, bool):
            raise ValueError("Completed status must be a boolean.")
        self.completed = value

    @classmethod
    def create(cls, session, name, category_id=None):
        """Create a new task."""
        if not name:
            raise ValueError("Task name cannot be empty.")
        task = cls(name=name, category_id=category_id)
        session.add(task)
        session.commit()
        return task

    @classmethod
    def delete(cls, session, task_id):
        """Delete a task by its ID."""
        task = session.query(cls).filter_by(id=task_id).first()
        if task:
            session.delete(task)
            session.commit()
        else:
            raise ValueError(f"Task with ID {task_id} not found.")

    @classmethod
    def get_all(cls, session):
        """Get all tasks."""
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, task_id):
        """Find a task by its ID."""
        return session.query(cls).filter_by(id=task_id).first()

    def __repr__(self):
        return f"<Task(id={self.id}, name={self.name}, completed={self.completed})>"

# Create an SQLite engine and session
engine = create_engine('sqlite:///tasks.db', echo=True)  # Example SQLite database
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables if they don't exist yet
Base.metadata.create_all(engine)
