from flask import render_template, request, redirect, url_for
from . import xss_bp

comments = []

@xss_bp.route("/level1")
def level1_theory():
    return render_template('xss/level1_theory.html')

@xss_bp.route("/level1/practice", methods=["GET", "POST"])
def level1_practice():
    if request.method == "POST":
        comment = request.form.get('comment', '')
        return render_template('xss/level1_practice.html', comment=comment)
    return render_template('xss/level1_practice.html', comment=None)

@xss_bp.route("/level2")
def level2_theory():
    return render_template('xss/level2_theory.html')

@xss_bp.route("/level2/practice", methods=["GET", "POST"])
def level2_practice():
    if request.method == "POST":
        comment = request.form.get('comment', '')
        comments.append(comment)
        return redirect(url_for('xss.level2_practice'))
    return render_template('xss/level2_practice.html', comments=comments)

@xss_bp.route("/level3")
def level3_theory():
    return render_template('xss/level3_theory.html')

@xss_bp.route("/level3/practice", methods=["GET", "POST"])
def level3_practice():
    if request.method == "POST":
        comment = request.form.get('comment', '')
        sanitized_comment = comment.replace('<script>', '').replace('</script>', '')
        comments.append(sanitized_comment)
        return redirect(url_for('xss.level3_practice'))
    return render_template('xss/level3_practice.html', comments=comments)

@xss_bp.route("/delete_comments", methods=["POST"])
def delete_comments():
    comments.clear()
    return redirect(url_for('main_page'))
