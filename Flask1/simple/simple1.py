from flask import Flask, redirect, url_for


app = Flask(__name__)

@app.route("/")

def home():
    return 'Hello! Welcome to Flask.'

@app.route("/<name>")
def user(name):
    return f"Hello {name}"


# redirect URL to another fuction i.e. --> home
@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()


