from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello():
    author = "Quang"
    read_val = 10

    if request.method == 'POST':
        if request.form["submit"] == "Turn light ON":
            print("TURN ON")
        elif request.form["submit"] == "Turn light OFF":
            print("TURN OFF")
        else:
            pass

    return render_template("hello.html", author=author, value=100*(read_val/1023.))


if __name__ == "__main__":
    app.run(debug=True)