
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(
        debug=False,
        host=app.config.get("HOST", "192.168.2.9"),
        port=app.config.get("PORT", 5000)
    )
