from flask import Flask

app = Flask(__name__, static_folder='Static')

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()