from flask import render_template, request
from . import rce_bp
import os

@rce_bp.route("/complex")
def complex_theory():
    return render_template('rce/complex_theory.html')

@rce_bp.route("/complex/practice", methods=["GET", "POST"])
def complex_practice():
    if request.method == "POST":
        env_var = request.form.get('env_var', '')
        try:
            # Уязвимый код: выполнение команды с пользовательским вводом
            command = f"echo {env_var}"
            result = os.popen(command).read()
        except Exception as e:
            result = f"Ошибка при выполнении команды: {e}"
        return render_template('rce/complex_practice.html', result=result)
    return render_template('rce/complex_practice.html', result=None)
