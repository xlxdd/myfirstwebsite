from flask import Flask

# static_url_path=,static_folder=,template_folder=
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
