from flask import Flask, render_template

app = Flask(__name__, static_folder='Static')

@app.route('/')
def home():
    return render_template('index.html')  # Rendering the 'index.html' template

if __name__ == '__main__':
    app.run(debug=True)