from datetime import datetime

from sqlalchemy.exc import IntegrityError

from database import db
from models import Task


def create_task(title, description):
    """Создает задачу в базе данных, используя текущее время"""
    now = datetime.now()  # Получаем текущую дату и время
    try:
        # создаем объект Task исходя из модели базы данных
        task = Task(
            title=title,
            description=description,
            created_at=now)

        # добавляем в базу данных
        db.session.add(task)
        db.session.commit()

        return {"id": task.id, "status": "Created"}, 201

    except IntegrityError as interror:
        # Возврашаем ошибку и ее описание при ошибке записи в базу данных
        return {'error': interror}, 400


def get_task(task_id):
    """Получаем отдельную статью из базы в JSON формате"""
    task = db.session.get(Task, task_id)  # Получаем запись по id
    if task:
        return task.to_dict(), 200
    return "not found", 404


def get_tasks():
    """Возвращает все задачи"""
    total = Task.query.all()
    return [i.to_dict() for i in total]


def update_task(task_id, title, description):
    """Обновляем задачу в базе данных"""

    task = db.session.get(Task, task_id)  # Получаем задачу из базы данных
    if task:
        # Вариант 1 - переписываем все данные по задаче
        now = datetime.now()  # Получаем текущее время для записи изменения
        task.title = title
        task.description = description
        task.updated_at = now  # Переписываем только время изменения
        db.session.commit()  # записываем изменения в базу данных
        return task.to_dict(), 201
    return "Задача не существует", 404


def delete_task(task_id):
    """Удаляет задачу из базы"""
    task = db.session.get(Task, task_id)  # Получаем задачу из базы данных, используя функцию из этого же компонента
    if task:
        db.session.delete(task)
        db.session.commit()
        return f'Задача с id {task_id} удалена', 204
    return f'Такой задачи нет', 404
