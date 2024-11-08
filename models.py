from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=False, nullable=False)
    password = db.Column(db.String(128), unique=False, nullable=False)

    @staticmethod
    def init_db():
        if not User.query.filter_by(username='admin').first():
            admin_user = User(username='admin', password='adminpass')
            db.session.add(admin_user)
        if not User.query.filter_by(username='user').first():
            user = User(username='user', password='userpass')
            db.session.add(user)
        db.session.commit()
