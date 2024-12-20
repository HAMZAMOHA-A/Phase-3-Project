# lib/db/models.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    
    # One-to-many relationship with Task
    tasks = relationship('Task', back_populates='category')

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Relationship with Category
    category = relationship('Category', back_populates='tasks')

    def __repr__(self):
        status = "Completed" if self.completed else "Pending"
        return f"<Task(id={self.id}, name={self.name}, completed={status})>"
