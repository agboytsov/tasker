from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Инициализируем SQLALchemy

# Добавляем к SQLAlchemy приложение
def init_app(app):
    db.init_app(app)
