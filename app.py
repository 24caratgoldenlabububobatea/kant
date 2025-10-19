from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("hjemmeside.html")

@app.route('/meny')
def meny():
    return render_template("meny.html")

@app.route('/varer')
def varer():
    return render_template("varer.html")

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(debug=True)
