from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/pag.1.html")
def pagina1():
    return render_template("pag.1.html")

@app.route("/pag.2.html")
def pagina2():
    return render_template("pag.2.html")

if __name__ == "__main__":
    app.run(debug=True)