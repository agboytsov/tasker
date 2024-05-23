import datetime

from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column

from database import db


class Task(db.Model):
    """Создаем основной класс задач, отражает одну конкретную задачу"""

    id: Mapped[int] = mapped_column(primary_key=True)  # Индекс строки
    title: Mapped[str] = mapped_column(String(256))  # Для str в Mysql требуется указание либо размера через String,
    # либо Text
    description: Mapped[str] = mapped_column(Text(),
                                             nullable=True)  # Задача может быть без описания
    created_at: Mapped[datetime.datetime]  # Обязательное поле, т.к. задача когда-то же создана
    updated_at: Mapped[datetime.datetime] = mapped_column(
        nullable=True)  # Не обязательное поле, т.к. задача могла и не меняться

    def to_dict(self):
        """Метод класса, возвращающий строку базы в виде словаря"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
