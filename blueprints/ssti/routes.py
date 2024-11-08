from flask import render_template, request, render_template_string
from . import ssti_bp

@ssti_bp.route("/level1")
def level1_theory():
    return render_template('ssti/level1_theory.html')

@ssti_bp.route("/level1/practice")
def level1_practice():
    name = request.args.get('name', '')
    # Уязвимый код: использование render_template_string с пользовательским вводом
    template = f"Привет, {name} <p>Используйте параметр name в URL</p>"
    return render_template_string(template)

@ssti_bp.route("/level2")
def level2_theory():
    return render_template('ssti/level2_theory.html')

@ssti_bp.route("/level2/practice")
def level2_practice():
    name = request.args.get('name', '')
    try:
        if name.isdigit():
            template = '''
            <p>В прошлом были цифры, теперь так нельзя</p>
            <p>Используйте параметр name в URL</p>
            '''
            return render_template_string(template)
        template = f'''
        <p>Теперь получи что-нибудь сложнее</p>
        Добро пожаловать, {name}
        <p>Используйте параметр name в URL</p>
        '''
        return render_template_string(template)
    except Exception as e:
        return f"Произошла ошибка: {e}", 500
