from flask import Flask, send_from_directory, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/app/<path:filename>')
def app_static(filename):
    return send_from_directory('app', filename)


@app.route('/node_modules/<path:filename>')
def node_modules_static(filename):
    return send_from_directory('node_modules', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
