"""
Flask app to give web interface for pyplico
"""


from flask import Flask
app = Flask(__name__)



@app.route('/')
def home():
    return '<h3>pyPlico home</h3>'


if __name__ == "__main__":
    app.run()