from flask import Flask, send_from_directory

application = Flask(__name__, static_folder='.')

@application.route('/')
def home():
    return send_from_directory('.', 'index.html')

@application.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    application.run()
