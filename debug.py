# debug.py

# debug.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

# Add the following line to start debugging
import ipdb; ipdb.set_trace()

if __name__ == "__main__":
    app.run(port=5555)
