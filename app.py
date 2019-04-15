from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def main():
    return send_file('./index.html')
@app.route('/hello')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
