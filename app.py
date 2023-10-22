from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return a friendly greeting."""
    return "Hello TechStars!"

if __name__ == '__main__':
    app.run()