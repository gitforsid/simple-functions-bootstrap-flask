from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def nav():
    return render_template("nav.html")


@app.route('/plates')
def plates():
    return render_template("plates.html")


@app.route('/text')
def text():
    return render_template("text.html")


@app.route('/tables')
def tables():
    return render_template("tables.html")


@app.route('/button')
def button():
    return render_template("button.html")


@app.route('/forms')
def forms():
    return render_template("forms.html")


@app.route('/pictures_font')
def pictures_font():
    return render_template("pictures_font.html")


@app.route('/text_panels')
def text_panels():
    return render_template("text_panels.html")


@app.route('/exit_panels')
def exit_panels():
    return render_template("exit_panels.html")


@app.route('/exit_form')
def exit_form():
    return render_template("exit_form.html")


@app.route('/modal_windows')
def modal_windows():
    return render_template("modal_windows.html")


@app.route('/nav_new')
def nav_new():
    return render_template("nav_new.html")


@app.route('/hint')
def hint():
    return render_template("hint.html")


if __name__ == '__main__':
    app.run()
