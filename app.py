from flask import Flask, send_file, send_from_directory, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return send_file('./index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/queryStatus')
def queryStatus():
    print('Query Status')
    return jsonify({'avl': 50, 'inflt': 10 })


if __name__ == '__main__':
    app.run()
