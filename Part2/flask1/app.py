from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    messages = [ "Welcome to my Flask App!", 
                "欢迎来到我的Flask应用!",
                "私のFlaskアプリへようこそ!", 
                "ยินดีต้อนรับสู่แอป Flask ของฉัน!", 
                "내 Flask 앱에 오신 것을 환영합니다!",
                "Bienvenue dans mon application Flask!",
                "Willkommen in meiner Flask-Anwendung!"]
    random_message = random.choice(messages)
    return render_template('index.html', random_message=random_message)

@app.route('/about')
def about():
    return 'This is a simple Flask application with random messages in different languages.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')