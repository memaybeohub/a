from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Xin chào từ Render.com!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000) # Cổng 10000 được Render.com yêu cầu
