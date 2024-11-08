from flask import render_template, request
from . import sqli_bp
from extensions import db
from sqlalchemy import text

@sqli_bp.route("/level1")
def level1_theory():
    return render_template('sqli/level1_theory.html')

@sqli_bp.route("/level1/practice", methods=["GET", "POST"])
def level1_practice():
    if request.method == "POST":
        name = request.form.get('name', '')
        # Уязвимый код: конкатенация строк
        query = f"SELECT * FROM user WHERE username = '{name}'"
        result = db.session.execute(text(query))
        data = result.fetchall()
        return render_template('sqli/level1_practice.html', data=data)
    return render_template('sqli/level1_practice.html', data=None)

@sqli_bp.route("/level2")
def level2_theory():
    return render_template('sqli/level2_theory.html')

@sqli_bp.route("/level2/practice", methods=["GET", "POST"])
def level2_practice():
    if request.method == "POST":
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        # Уязвимый код: конкатенация строк с несколькими параметрами
        query = f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'"
        result = db.session.execute(text(query))
        data = result.fetchall()
        return render_template('sqli/level2_practice.html', data=data)
    return render_template('sqli/level2_practice.html', data=None)

@sqli_bp.route("/level3")
def level3_theory():
    return render_template('sqli/level3_theory.html')

@sqli_bp.route("/level3/practice", methods=["GET", "POST"])
def level3_practice():
    if request.method == "POST":
        user_id = request.form.get('user_id', '')
        # Уязвимый код: вставка пользовательского ввода без проверки типа
        query = f"SELECT * FROM user WHERE id = {user_id}"
        try:
            result = db.session.execute(text(query))
            data = result.fetchall()
        except Exception as e:
            data = str(e)
        return render_template('sqli/level3_practice.html', data=data)
    return render_template('sqli/level3_practice.html', data=None)

@sqli_bp.route("/level3hard")
def level3hard_theory():
    return render_template('sqli/level3hard_theory.html')

@sqli_bp.route("/level3hard/practice", methods=["GET", "POST"])
def level3hard_practice():
    if request.method == "POST":
        user_id = request.form.get('user_id', '')
        # Уязвимость из-за неправильного преобразования данных
        query = text("SELECT * FROM user WHERE id = :id")
        result = db.session.execute(query, {'id': user_id})
        data = result.fetchall()
        return render_template('sqli/level3hard_practice.html', data=data)
    return render_template('sqli/level3hard_practice.html', data=None)
