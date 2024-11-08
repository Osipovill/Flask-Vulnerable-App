import subprocess
from flask import Flask, render_template
from loguru import logger

from extensions import db
from config import Config
from blueprints.xss import xss_bp
from blueprints.sqli import sqli_bp
from blueprints.ssti import ssti_bp
from blueprints.rce import rce_bp
from models import User


def create_app():
    logger.info("Инициализация приложения Flask")
    app = Flask(__name__, template_folder='src', static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)
    logger.info("Инициализация расширения SQLAlchemy")

    app.register_blueprint(xss_bp)
    app.register_blueprint(sqli_bp)
    app.register_blueprint(ssti_bp)
    app.register_blueprint(rce_bp)
    logger.info("Регистрация всех Blueprints завершена")

    @app.route("/")
    def main_page():
        logger.info("Главная страница загружена")
        return render_template('main_menu.html')

    @app.route('/scan')
    def scan():
        return render_template('scan.html')

    return app

def run_tests():
    """Функция для запуска тестов с покрытием и вывода результата"""
    logger.info("Запуск тестов с покрытием кода...")

    result = subprocess.run(
        [
            'pytest',
            '--cov=app',
            '--cov-report=term-missing'
        ],
        capture_output=True, text=True
    )
    logger.info(f"Тестирование:\n{result.stdout}")
    if result.returncode != 0:
        logger.error("Некоторые тесты не прошли.")
    else:
        logger.info("Все тесты успешно пройдены.")


if __name__ == '__main__':
    run_tests()
    app = create_app()

    with app.app_context():

        db.create_all()
        logger.info("Создание таблиц базы данных завершено")

        User.init_db()
        logger.info("Инициализация начальных данных в базе данных завершена")

    logger.info("Запуск приложения Flask")
    app.run(host="0.0.0.0", port=8081, debug=False)
