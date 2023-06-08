from flask import Flask, render_template

# static_url_path=,static_folder=,template_folder=
app = Flask(__name__)
app.debug = True

@app.route('/')
def login():  # put application's code here
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug = True)
