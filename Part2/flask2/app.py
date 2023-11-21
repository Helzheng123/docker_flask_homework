from flask import Flask, render_template
import random

app = Flask(__name__)

#in Celsius

@app.route('/')
def home():
    cities = [
        {"name": "New York", "temperature": random.randint(0, 30), "condition": "Sunny"},
        {"name": "Paris", "temperature": random.randint(10, 25), "condition": "Cloudy"},
        {"name": "Tokyo", "temperature": random.randint(15, 30), "condition": "Rainy"},
        {"name": "Sydney", "temperature": random.randint(20, 35), "condition": "Clear"},
        {"name": "Moscow", "temperature": random.randint(-10, 10), "condition": "Snowy"},
    ]

    random_city = random.choice(cities)
    return render_template('about.html', city=random_city)

@app.route('/about')
def about():
    return 'This is a simple Flask application with different countries and random weather information.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')