import os
from dotenv import load_dotenv

load_dotenv() # загружаем переменные из .env файла в среду выполнения
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Конфиг подключения к базе данных"""

    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')

    # формируем строку с адресом базы данных
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    # Указываем папку миграций
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')

class TestingConfig:
    """Тестовый конфиг для pytest"""

    DB_USER = os.getenv('DB_USER_TEST')
    DB_PASSWORD = os.getenv('DB_PASSWORD_TEST')
    DB_NAME = os.getenv('DB_NAME_TEST')
    print(DB_NAME)
    DB_HOST = os.getenv('DB_HOST_TEST')
    DB_PORT = os.getenv('DB_PORT_TEST')

    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
