from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('base.html')

@app.route('/contactus')
def contact_us(): 
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')