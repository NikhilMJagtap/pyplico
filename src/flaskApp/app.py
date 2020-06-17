"""
Flask app to give web interface for pyplico
"""
from flask import Flask
from flask import render_template

app = Flask(
        __name__, 
        static_url_path='', 
        static_folder='public', 
        template_folder='public/html'
    )

DEBUG = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyse')
def analyse():
    return render_template('analyse.html')

if __name__ == "__main__":
    app.run(debug=DEBUG)