import json
from datetime import datetime
from bson.objectid import ObjectId

from db import db


collection = db['tasks']


class Task:
    def __init__(self, title, _id=None, description=None, completed=False, created_at=None) -> None:
        self._id = _id if _id else ObjectId()
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at if created_at else datetime.now()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value:
                setattr(self, key, value)
        return collection.update_one({"_id": self._id}, {"$set": self.__dict__})

    def save(self, update=False, **kwargs):
        if update:
            return self.update(**kwargs)
        return collection.insert_one(self.__dict__)

    @property
    def __dict__(self):
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }

    def __str__(self) -> str:
        return f"Task object {self._id}"

    def json(self, multiple=False):
        task = self.__dict__
        task['_id'] = str(task.pop("_id"))
        task['created_at'] = task.pop('created_at').isoformat()
        if multiple:
            return task
        return json.dumps(task, indent=4)


def create_task(task: Task):
    return task.save()


def get_tasks(pretty=False):
    tasks = [Task(**task) for task in collection.find()]
    if pretty:
        tasks = json.dumps([task.json(multiple=True) for task in tasks], indent=4)
    return tasks


def update_task(task: Task, title=None, description=None, completed=None):
    task.save(title=title, description=description,
              completed=completed, update=True)


def delete_task(id):
    collection.delete_one({"_id": id})
