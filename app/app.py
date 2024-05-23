from flasgger import Swagger
from flask import Flask
from flask_migrate import Migrate

import database
from api import api
from front import front


def create_app():
    app = Flask(__name__)

    # Берем данные конфига, включаем перезагрузку приложения при изменении файлов
    app.config.from_object('config.Config')
    app.debug = True
    # Устанавливаем все, связанное с базой, предусматриваем миграции
    database.init_app(app)
    Migrate(app, database.db)
    #
    # добавляем роуты - для api и для html
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(front)
    app.config['SWAGGER'] = {
        'title': 'Тестовое API для задачника',
        'description': 'Реализован базовый CRUD функционал по задачам. Дополнительно есть фронт интерфейс, swagger, docker'
    }
    Swagger(app)
    # app.register_blueprint(app2, url_prefix="/app2")

    return app


# запускаем
if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=5000)
