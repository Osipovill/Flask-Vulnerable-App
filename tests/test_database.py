import pytest
from app import create_app, db
from models import User

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        User.init_db()
        yield app
        db.session.remove()
        db.drop_all()

def test_database_initialization(app):
    """Проверяет, что таблицы базы данных создаются и инициализируются корректно"""
    with app.app_context():
        users = User.query.all()
        assert len(users) > 0
