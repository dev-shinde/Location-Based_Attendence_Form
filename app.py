from flask import *

app = Flask(__name__)

@app.route('/')
def submit_form():
    return render_template("form.html")

@app.route("/hello")
def form():
    return render_template("NEW.html")

if __name__ == '__main__':
    app.run(debug=True)
