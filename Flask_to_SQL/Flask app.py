from flask import Flask
from flask_cors import CORS
from Functions import Functions

app = Flask(__name__)
app.register_blueprint(Functions, url_prefix='/Functions')
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, port=8000)