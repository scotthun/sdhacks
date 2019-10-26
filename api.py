from flask import Flask
import youtube
app = Flask(__name__)

@app.route('/')
def index():
    youtube.castVideo()
    return "Hello, World!"

#http://localhost:5000/

if __name__ == '__main__':
    app.run(debug=True)